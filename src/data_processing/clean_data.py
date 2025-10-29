"""
Data Cleaning Script
Processes commodity prices, climate data, trade data, IIP, WPI, GDP, and OECD data
Based on data_cleaning.ipynb notebook implementation
"""

import pandas as pd
import numpy as np
import pycountry
import pycountry_convert as pc
import polars as pl
from pathlib import Path
from typing import Dict, List

# Configuration
HUGGINGFACE_TOKEN = "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"
DATA_DIR = Path("./data")
RAW_DIR = DATA_DIR / "raw"
PROCESSED_DIR = DATA_DIR / "processed"

# Ensure directories exist
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)


def clean_commodity_prices() -> pd.DataFrame:
    """Clean and process CMO monthly commodity price data"""
    print("Processing commodity prices...")

    # URLs
    cmoMonthlyPrices = "https://huggingface.co/datasets/aaronmat1905/ADA_Project_Data/resolve/main/raw/commodity_prices/extracted/cmoMonthly_monthly_prices.csv"

    # Read CSV, skip metadata
    cmo1 = pd.read_csv(cmoMonthlyPrices, skiprows=6)

    # Columns to keep
    cols = ["5", "Unnamed: 1", "CRUDE_PETRO", "WHEAT_US_HRW", "RICE_05", "COPPER", "ALUMINUM"]

    # Keep rows where 'Unnamed: 1' matches YYYYMM pattern
    cmo1_valid = cmo1[cmo1["Unnamed: 1"].astype(str).str.match(r"^\d{4}M\d{2}$")].copy()

    # Select relevant columns and rename date
    cmo1_final = cmo1_valid[cols].rename(columns={"Unnamed: 1": "Date"})

    # Parse Date from 'YYYYMmm' format
    cmo1_final["Date"] = cmo1_final["Date"].apply(
        lambda x: pd.Timestamp(year=int(x[:4]), month=int(x[5:]), day=1)
    )

    # Filter for 2010-2024
    cmo1_final = cmo1_final[
        (cmo1_final["Date"].dt.year >= 2010) & (cmo1_final["Date"].dt.year <= 2024)
    ]

    # Calculate log returns
    for col in cols[2:]:
        cmo1_final[col + '_logret'] = np.log(cmo1_final[col] / cmo1_final[col].shift(1))

    # Calculate rolling volatility
    windows = [3, 6, 12]
    for col in cols[2:]:
        for w in windows:
            cmo1_final[f"{col}_vol_{w}m"] = cmo1_final[col + '_logret'].rolling(w).std()

    # Create shock indicators
    for col in cols[2:]:
        cmo1_final[f"{col}_shock"] = (
            np.abs(cmo1_final[col + '_logret']) > 2 * cmo1_final[col + '_logret'].std()
        ).astype(int)

    cmo1_final.reset_index(drop=True, inplace=True)

    # Save
    output_path = PROCESSED_DIR / "proc_cmo_monthly.csv"
    cmo1_final.to_csv(output_path, index=False)
    print(f"✓ Saved commodity prices: {output_path}")

    return cmo1_final


def clean_climate_data() -> pd.DataFrame:
    """Clean and process ONI climate data"""
    print("\nProcessing climate data...")

    oni_df = pd.read_csv(
        "https://huggingface.co/datasets/aaronmat1905/ADA_Project_Data/resolve/main/raw/instruments/Monthly%20Oceanic%20Nino%20Index%20(ONI)%20-%20Wide.csv"
    )

    # Melt to long format
    oni_long = oni_df.melt(id_vars=['Year'], var_name='Month', value_name='ONI')

    # Map month names
    month_map = {
        'DJF': 1, 'JFM': 1, 'FMA': 2, 'MAM': 3, 'AMJ': 4, 'MJJ': 5,
        'JJA': 6, 'JAS': 7, 'ASO': 8, 'SON': 9, 'OND': 10, 'NDJ': 11
    }
    oni_long['Month_num'] = oni_long['Month'].map(month_map)
    oni_long['Date'] = pd.to_datetime(
        dict(year=oni_long['Year'], month=oni_long['Month_num'], day=1)
    )

    # Filter for 2010-2024
    start_year, end_year = 2010, 2024
    oni_filtered = oni_long[
        (oni_long['Date'].dt.year >= start_year) &
        (oni_long['Date'].dt.year <= end_year)
    ].copy()

    # Classify ENSO Phases
    def classify_enso(oni):
        if oni >= 0.5:
            return 'El Nino'
        elif oni <= -0.5:
            return 'La Nina'
        else:
            return 'Neutral'

    oni_filtered["ENSO_Phase"] = oni_filtered["ONI"].apply(classify_enso)

    # Apply lag variables
    oni_filtered = oni_filtered.sort_values("Date").reset_index(drop=True)
    for lag in [1, 3, 6]:
        oni_filtered[f"ONI_lag_{lag}m"] = oni_filtered["ONI"].shift(lag)

    # Save
    output_path = PROCESSED_DIR / "climate_oni_clean.csv"
    oni_filtered.to_csv(output_path, index=False)
    print(f"✓ Saved climate data: {output_path}")

    return oni_filtered


def clean_trade_data() -> pd.DataFrame:
    """Clean and process bilateral trade data"""
    print("\nProcessing trade data...")

    TARGET_PARTNERS = ['United States', 'China', 'Saudi Arabia', 'UAE',
                       'Qatar', 'Germany', 'France', 'Italy']

    COMMODITY_MAPPING = {
        'Energy': ['27'],
        'Food': ['10', '11'],
        'Metals': ['74', '76']
    }

    def map_commodity_group(indicator):
        if indicator is None:
            return 'Other'
        hs_code = str(indicator)[:2]
        for group, codes in COMMODITY_MAPPING.items():
            if hs_code in codes:
                return group
        return 'Other'

    # Read and process with Polars
    tradeDf = pl.scan_csv(str(RAW_DIR / "IMTSTrade.csv"))
    tradeDf = tradeDf.filter(
        (pl.col('COUNTRY').str.contains('India')) &
        (pl.col('COUNTERPART_COUNTRY').is_in(TARGET_PARTNERS))
    )

    tradeDf = tradeDf.collect()
    tradeDf = tradeDf.with_columns(
        pl.col('INDICATOR').map_elements(map_commodity_group).alias('commodity_group')
    )

    # Get 2010-2024 monthly columns
    date_cols = [col for col in tradeDf.columns
                 if '-M' in str(col) and 2010 <= int(str(col).split('-')[0]) <= 2024]

    keep_cols = ['COUNTRY', 'COUNTERPART_COUNTRY', 'TRADE_FLOW', 'commodity_group'] + date_cols
    tradeDf = tradeDf.select(keep_cols)

    # Convert wide to long
    df_long = tradeDf.unpivot(
        index=['COUNTRY', 'COUNTERPART_COUNTRY', 'TRADE_FLOW', 'commodity_group'],
        on=date_cols,
        variable_name='date',
        value_name='trade_value_usd'
    )

    # Save
    output_path = PROCESSED_DIR / "trade_india_bilateral.csv"
    df_long.write_csv(str(output_path))
    print(f"✓ Saved trade data: {output_path}")

    return df_long.to_pandas()


def create_country_mapping() -> pd.DataFrame:
    """Create country ISO3 and region mappings"""
    print("\nCreating country mapping...")

    # Load WITS data
    wits_df = pd.read_excel(RAW_DIR / "WITS-Partner.xlsx", sheet_name="Partner")

    # Extract unique country names
    reporters = wits_df[['Reporter Name']].rename(columns={'Reporter Name': 'Country Name'})
    partners = wits_df[['Partner Name']].rename(columns={'Partner Name': 'Country Name'})
    country_list = pd.concat([reporters, partners]).drop_duplicates().reset_index(drop=True)

    # Functions to get ISO3 and region
    def get_iso3(name):
        try:
            return pycountry.countries.lookup(name).alpha_3
        except:
            return None

    def get_region(name):
        try:
            iso = pycountry.countries.lookup(name).alpha_2
            continent_code = pc.country_alpha2_to_continent_code(iso)
            return pc.convert_continent_code_to_continent_name(continent_code)
        except:
            return None

    country_list["ISO3"] = country_list["Country Name"].apply(get_iso3)
    country_list["Region"] = country_list["Country Name"].apply(get_region)

    # Save
    output_path = PROCESSED_DIR / "country_mapping.csv"
    country_list.to_csv(output_path, index=False)
    print(f"✓ Saved country mapping: {output_path}")

    return country_list


def clean_iip_data() -> pd.DataFrame:
    """Clean Index of Industrial Production data"""
    print("\nProcessing IIP data...")

    iip_path = RAW_DIR / "IndexofIndustrialProduction.xlsx"
    baseYear11_12 = pd.read_excel(iip_path, sheet_name="IIP-Industry-Base 2011-12")

    # Clean and prepare data
    baseYear11_12 = baseYear11_12.drop([0, 1, 2, 3])
    baseYear11_12.columns = baseYear11_12.iloc[0]
    baseYear11_12 = baseYear11_12[1:]
    baseYear11_12 = baseYear11_12.reset_index(drop=True)
    baseYear11_12 = baseYear11_12.drop([23, 24, 25])
    baseYear11_12 = baseYear11_12.reset_index(drop=True)
    baseYear11_12 = baseYear11_12.drop(baseYear11_12.columns[0], axis=1)
    baseYear11_12 = baseYear11_12.rename(columns={'4': 'sl_no'})

    # Clean column names
    baseYear11_12.columns = ['sector_name'] + [
        col.split(' ')[0].replace(':', '-')
        for col in baseYear11_12.columns[1:]
    ]

    # Melt to long format
    date_cols = [col for col in baseYear11_12.columns if col != 'sector_name']
    baseYear11_12_long = baseYear11_12.melt(
        id_vars=['sector_name'],
        value_vars=date_cols,
        var_name='date',
        value_name='iip_index'
    )

    # Convert types
    baseYear11_12_long['iip_index'] = pd.to_numeric(
        baseYear11_12_long['iip_index'], errors='coerce'
    )
    baseYear11_12_long['date'] = pd.to_datetime(
        baseYear11_12_long['date'], format='%Y-%m'
    )

    # Filter 2010-2024
    baseYear11_12_long = baseYear11_12_long[
        (baseYear11_12_long['date'] >= '2010-01') &
        (baseYear11_12_long['date'] <= '2024-12')
    ]

    # Calculate growth rates
    baseYear11_12_long = baseYear11_12_long.sort_values(
        ['sector_name', 'date']
    ).reset_index(drop=True)
    baseYear11_12_long['iip_mom_growth'] = baseYear11_12_long.groupby(
        'sector_name'
    )['iip_index'].pct_change() * 100
    baseYear11_12_long['iip_yoy_growth'] = baseYear11_12_long.groupby(
        'sector_name'
    )['iip_index'].pct_change(12) * 100

    # Energy-intensive flag
    energy_sectors = [
        'Manufacture of chemicals and chemical products',
        'Manufacture of basic metals',
        'Manufacture of coke and refined petroleum prod'
    ]
    baseYear11_12_long['is_energy_intensive'] = baseYear11_12_long[
        'sector_name'
    ].isin(energy_sectors)

    # Save
    output_path = PROCESSED_DIR / "iip_sectoral.csv"
    baseYear11_12_long.to_csv(output_path, index=False)
    print(f"✓ Saved IIP data: {output_path}")

    return baseYear11_12_long


def clean_wpi_data() -> pd.DataFrame:
    """Clean Wholesale Price Index data"""
    print("\nProcessing WPI data...")

    wpi_path = RAW_DIR / "WholesalePriceIndexMonthlyData.xlsx"
    wpi_df = pd.read_excel(wpi_path, sheet_name="WPI Index (Base 2011-12)", header=5)
    wpi_df = wpi_df.drop(wpi_df.columns[0], axis=1)
    wpi_df = wpi_df.drop([869, 870, 871])

    # Keep specific categories
    keep_categories = [
        'II FUEL & POWER',
        'III   MANUFACTURED PRODUCTS',
        '(A).  FOOD ARTICLES'
    ]

    wpi_filtered = wpi_df[wpi_df['Commodity Description'].isin(keep_categories)].copy()

    # Reshape to long format
    date_cols = [col for col in wpi_filtered.columns
                 if col not in ["Community Description", "Commodity Weight"]]
    wpi_long = wpi_filtered.melt(
        id_vars=["Commodity Description"],
        value_vars=date_cols,
        var_name='date',
        value_name="wpi_index"
    )

    # Clean dates
    wpi_long["date"] = pd.to_datetime(wpi_long['date'], format="%b-%Y")
    wpi_long = wpi_long[
        (wpi_long['date'] >= '2010-01') & (wpi_long['date'] <= '2024-12')
    ]

    # Calculate inflation
    wpi_long = wpi_long.sort_values(["Commodity Description", 'date'])
    wpi_long['wpi_inflation'] = wpi_long.groupby(
        'Commodity Description'
    )['wpi_index'].pct_change(12) * 100
    wpi_long.columns = ["category", "date", "wpi_index", "wpi_inflation"]

    # Save
    output_path = PROCESSED_DIR / "wpi_inflation.csv"
    wpi_long.to_csv(output_path, index=False)
    print(f"✓ Saved WPI data: {output_path}")

    return wpi_long


def clean_gdp_data() -> pd.DataFrame:
    """Clean GDP quarterly estimates"""
    print("\nProcessing GDP data...")

    def create_date(row, year_col):
        year_str = str(row[year_col])
        quarter = row['Quarter']

        if year_str == 'nan' or pd.isna(quarter):
            return None

        year = int(year_str.split('-')[0])
        q_map = {'Q1': '04', 'Q2': '07', 'Q3': '10', 'Q4': '01'}
        month = q_map[quarter]

        if quarter == 'Q4':
            year += 1

        return f"{year}-{month}-01"

    # Read constant and current price GDP
    constant_path = RAW_DIR / "GDP_Constant.xlsx"
    current_path = RAW_DIR / "GDP_Current.xlsx"

    constantDF = pd.read_excel(constant_path, sheet_name="NAS  2011-12")
    constantDF = constantDF.drop([0, 1, 2, 3, 5, 63, 64])
    constantDF = constantDF.drop(constantDF.columns[0], axis=1)
    constantDF.columns = constantDF.iloc[0]
    constantDF = constantDF[1:]
    constantDF = constantDF.reset_index(drop=True)

    currentDF = pd.read_excel(current_path, sheet_name="NAS  2011-12")
    currentDF = currentDF.drop([0, 1, 2, 3, 5, 63, 64])
    currentDF.columns = currentDF.iloc[0]
    currentDF = currentDF[1:]
    currentDF = currentDF.drop(currentDF.columns[0], axis=1)
    currentDF = currentDF.reset_index(drop=True)

    # Process dates
    constantDF['date'] = constantDF.apply(lambda row: create_date(row, 'date'), axis=1)
    currentDF['date'] = currentDF.apply(lambda row: create_date(row, 'date'), axis=1)

    # Drop NaN and convert
    for df in [constantDF, currentDF]:
        df.dropna(subset=['date'], inplace=True)
        df['date'] = pd.to_datetime(df['date'])

    # Keep only GDP column
    gdp_const = constantDF[['date', '9. Gross Domestic Product']].copy()
    gdp_const.columns = ['date', 'gdp_constant']

    gdp_curr = currentDF[['date', '9. Gross Domestic Product']].copy()
    gdp_curr.columns = ['date', 'gdp_current']

    # Merge
    gdp_merged = gdp_const.merge(gdp_curr, on='date')

    # Calculate YoY growth
    gdp_merged['gdp_growth_yoy'] = gdp_merged['gdp_constant'].pct_change(4) * 100

    # Filter 2010-2024
    gdp_merged = gdp_merged[
        (gdp_merged['date'] >= '2010-01') & (gdp_merged['date'] <= '2024-12')
    ]

    # Resample to monthly
    gdp_merged = gdp_merged.set_index('date').resample('MS').ffill().reset_index()

    # Save
    output_path = PROCESSED_DIR / "gdp_quarterly.csv"
    gdp_merged.to_csv(output_path, index=False)
    print(f"✓ Saved GDP data: {output_path}")

    return gdp_merged


def clean_oecd_data() -> pd.DataFrame:
    """Clean OECD global macro data"""
    print("\nProcessing OECD data...")

    df = pd.read_csv(RAW_DIR / 'OECD_file.csv', skiprows=1)

    oecd_clean = pd.DataFrame({
        'country': df.iloc[:, 4],
        'date': df.iloc[:, 20],
        'cpi_growth': df.iloc[:, 22]
    })

    oecd_clean['date'] = pd.to_datetime(oecd_clean['date'], format='%Y-%m')
    oecd_clean['cpi_growth'] = pd.to_numeric(oecd_clean['cpi_growth'], errors='coerce')

    # Remove G20 aggregate
    oecd_clean = oecd_clean[oecd_clean['country'] != 'G20']

    # Filter 2010-2024
    oecd_clean = oecd_clean[
        (oecd_clean['date'] >= '2010-01') & (oecd_clean['date'] <= '2024-12')
    ]

    # Pivot wide
    oecd_wide = oecd_clean.pivot(
        index='date', columns='country', values='cpi_growth'
    ).reset_index()

    # Calculate G20 average (excluding India)
    country_cols = [col for col in oecd_wide.columns if col not in ['date', 'India']]
    oecd_wide['g20_avg_cpi_growth'] = oecd_wide[country_cols].mean(axis=1)

    # Save
    output_path = PROCESSED_DIR / "global_macro.csv"
    oecd_wide.to_csv(output_path, index=False)
    print(f"✓ Saved OECD data: {output_path}")

    return oecd_wide


def main():
    """Run all data cleaning operations"""
    print("="*70)
    print("DATA CLEANING PIPELINE")
    print("="*70)

    # Run all cleaning functions
    clean_commodity_prices()
    clean_climate_data()
    clean_iip_data()
    clean_wpi_data()
    clean_gdp_data()
    clean_oecd_data()

    print("\n" + "="*70)
    print("DATA CLEANING COMPLETE!")
    print("="*70)
    print(f"\nProcessed files saved to: {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
