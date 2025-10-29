"""
Master Dataset Creation Script
Merges all processed data sources into a single master dataset
Based on create_master_dataset.ipynb notebook implementation
"""

import pandas as pd
import numpy as np
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration
DATA_DIR = Path("./data")
PROCESSED_DIR = DATA_DIR / "processed"
IO_DIR = DATA_DIR / "processed_io_data"


def load_all_datasets() -> dict:
    """Load all processed datasets"""
    print("="*70)
    print("LOADING ALL DATASETS")
    print("="*70)

    datasets = {}

    # 1. Commodity Prices
    datasets['commodity_prices'] = pd.read_csv(PROCESSED_DIR / 'proc_cmo_monthly.csv')
    datasets['commodity_prices'] = datasets['commodity_prices'].drop(columns=['Unnamed: 0'], errors='ignore')
    if 'Date' in datasets['commodity_prices'].columns:
        datasets['commodity_prices'] = datasets['commodity_prices'].rename(columns={'Date': 'date'})
    datasets['commodity_prices']['date'] = pd.to_datetime(datasets['commodity_prices']['date'])
    print(f"  ✓ Commodity prices: {datasets['commodity_prices'].shape}")

    # 2. Climate Data
    datasets['climate_oni'] = pd.read_csv(PROCESSED_DIR / 'climate_oni_clean.csv')
    datasets['climate_oni'] = datasets['climate_oni'].drop(columns=['Unnamed: 0'], errors='ignore')
    datasets['climate_oni']['Date'] = pd.to_datetime(datasets['climate_oni']['Date'])
    datasets['climate_oni'] = datasets['climate_oni'].rename(columns={'Date': 'date'})
    print(f"  ✓ Climate ONI: {datasets['climate_oni'].shape}")

    # 3. IIP Sectoral
    datasets['iip_sectoral'] = pd.read_csv(PROCESSED_DIR / 'iip_sectoral.csv')
    datasets['iip_sectoral']['date'] = pd.to_datetime(datasets['iip_sectoral']['date'])
    print(f"  ✓ IIP Sectoral: {datasets['iip_sectoral'].shape}")

    # 4. WPI Inflation
    datasets['wpi_inflation'] = pd.read_csv(PROCESSED_DIR / 'wpi_inflation.csv')
    datasets['wpi_inflation']['date'] = pd.to_datetime(datasets['wpi_inflation']['date'])
    print(f"  ✓ WPI Inflation: {datasets['wpi_inflation'].shape}")

    # 5. GDP Quarterly
    datasets['gdp_quarterly'] = pd.read_csv(PROCESSED_DIR / 'gdp_quarterly.csv')
    datasets['gdp_quarterly']['date'] = pd.to_datetime(datasets['gdp_quarterly']['date'])
    print(f"  ✓ GDP Quarterly: {datasets['gdp_quarterly'].shape}")

    # 6. Global Macro
    datasets['global_macro'] = pd.read_csv(PROCESSED_DIR / 'global_macro.csv')
    datasets['global_macro']['date'] = pd.to_datetime(datasets['global_macro']['date'])
    print(f"  ✓ Global Macro: {datasets['global_macro'].shape}")

    # 7. Trade Bilateral
    datasets['trade_bilateral'] = pd.read_csv(PROCESSED_DIR / 'trade_india_bilateral.csv')
    if 'date' not in datasets['trade_bilateral'].columns:
        date_col = [col for col in datasets['trade_bilateral'].columns
                   if 'M' in str(datasets['trade_bilateral'][col].iloc[0])]
        if date_col:
            datasets['trade_bilateral']['date'] = pd.to_datetime(
                datasets['trade_bilateral'][date_col[0]], format='%Y-M%m'
            )
    else:
        datasets['trade_bilateral']['date'] = pd.to_datetime(datasets['trade_bilateral']['date'])
    print(f"  ✓ Trade Bilateral: {datasets['trade_bilateral'].shape}")

    # 8. Network Metrics
    datasets['network_metrics'] = pd.read_csv(IO_DIR / 'network_metrics.csv')
    datasets['network_metrics'] = datasets['network_metrics'].drop(columns=['Unnamed: 0'], errors='ignore')
    print(f"  ✓ Network Metrics: {datasets['network_metrics'].shape}")

    print("\n✓ All datasets loaded successfully!")
    return datasets


def create_sector_mapping() -> dict:
    """Map IIP sectors to I-O sectors"""
    print("\nCreating sector mapping...")

    sector_mapping = {
        # Food & Beverages
        'Manufacture of food products': 'Miscellaneous food\n products',
        'Manufacture of beverages': 'Beverages',

        # Textiles & Apparel
        'Manufacture of textiles': 'Cotton textiles',
        'Manufacture of wearing apparel': 'Ready made garments',
        'Manufacture of leather and related products': 'Leather and leather\n products',

        # Wood, Paper, Printing
        'Manufacture of paper and paper products': 'Paper, Paper products and\n newsprint',
        'Printing and reproduction of recorded media': 'Publishing, printing and\n allied activities',

        # Chemicals & Petroleum
        'Manufacture of chemicals and chemical products': 'Other chemicals',
        'Manufacture of pharmaceuticals, medicinal chemical and botanical products': 'Drugs and medicine',
        'Manufacture of coke and refined petroleum products': 'Petroleum products',
        'Manufacture of rubber and plastics products': 'Plastic products',

        # Non-metallic minerals
        'Manufacture of other non-metallic mineral products': 'Cement',

        # Metals
        'Manufacture of basic metals': 'Iron and steel foundries',
        'Manufacture of fabricated metal products, except machinery and equipment': 'Miscellaneous metal\n products',

        # Machinery & Equipment
        'Manufacture of machinery and equipment n.e.c.': 'Other non-electrical\n machinery',
        'Manufacture of computer, electronic and optical products': 'Electronic\n equipments(incl.TV)',
        'Manufacture of electrical equipment': 'Electrical industrial\n Machinery',

        # Transport Equipment
        'Manufacture of motor vehicles, trailers and semi-trailers': 'Motor vehicles',
        'Manufacture of other transport equipment': 'Other transport\n equipments',

        # Other Manufacturing
        'Manufacture of furniture': 'Furniture & Fixtures',
        'Manufacture of tobacco products': 'Tobacco Products',
        'Other manufacturing': 'Miscellaneous\n manufacturing',
    }

    print(f"✓ Mapped {len(sector_mapping)} IIP sectors to I-O sectors")
    return sector_mapping


def merge_datasets(datasets: dict, sector_mapping: dict) -> pd.DataFrame:
    """Merge all datasets into master dataset"""
    print("\n" + "="*70)
    print("MERGING DATASETS")
    print("="*70)

    # Step 1: Apply sector mapping to IIP
    print("\n1. Applying sector mapping to IIP data...")
    iip_sectoral = datasets['iip_sectoral'].copy()
    iip_sectoral['io_sector_name'] = iip_sectoral['sector_name'].map(sector_mapping)
    iip_sectoral['io_sector_name'] = iip_sectoral['io_sector_name'].fillna(
        iip_sectoral['sector_name']
    )

    # Remove "General Index"
    before_count = len(iip_sectoral)
    iip_sectoral = iip_sectoral[iip_sectoral['sector_name'] != 'General Index'].copy()
    after_count = len(iip_sectoral)
    print(f"  ✓ Removed 'General Index': {before_count - after_count:,} rows")

    # Step 2: Merge IIP with Network Metrics
    print("\n2. Merging IIP with Network Metrics...")
    master_df = iip_sectoral.merge(
        datasets['network_metrics'],
        left_on='io_sector_name',
        right_on='sector_name',
        how='left',
        suffixes=('', '_io')
    )
    master_df = master_df.drop(columns=['sector_name_io'], errors='ignore')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 3: Merge Commodity Prices
    print("\n3. Merging Commodity Prices...")
    master_df = master_df.merge(datasets['commodity_prices'], on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 4: Merge Climate Data
    print("\n4. Merging Climate Data...")
    master_df = master_df.merge(datasets['climate_oni'], on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 5: Merge WPI Inflation (pivot to wide)
    print("\n5. Merging WPI Inflation...")
    wpi_wide = datasets['wpi_inflation'].pivot(
        index='date',
        columns='category',
        values='wpi_inflation'
    ).reset_index()
    wpi_wide.columns = ['date'] + [
        f'wpi_{col.lower().replace(" ", "_").replace("&", "and").replace(".", "")}'
        for col in wpi_wide.columns[1:]
    ]
    master_df = master_df.merge(wpi_wide, on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 6: Merge GDP Quarterly
    print("\n6. Merging GDP Quarterly...")
    master_df = master_df.merge(datasets['gdp_quarterly'], on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 7: Merge Global Macro
    print("\n7. Merging Global Macro...")
    master_df = master_df.merge(datasets['global_macro'], on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    # Step 8: Merge Trade Data (aggregated)
    print("\n8. Merging Trade Data...")
    trade_totals = datasets['trade_bilateral'].groupby('date').agg({
        'trade_value_usd': 'sum'
    }).reset_index()
    trade_totals.columns = ['date', 'total_trade_value']

    if 'commodity_group' in datasets['trade_bilateral'].columns:
        energy_trade = datasets['trade_bilateral'][
            datasets['trade_bilateral']['commodity_group'] == 'Energy'
        ].groupby('date')['trade_value_usd'].sum().reset_index()
        energy_trade.columns = ['date', 'energy_trade_value']
        master_df = master_df.merge(energy_trade, on='date', how='left')

    master_df = master_df.merge(trade_totals, on='date', how='left')
    print(f"  ✓ Shape: {master_df.shape}")

    return master_df


def create_derived_variables(master_df: pd.DataFrame) -> pd.DataFrame:
    """Create derived variables and feature engineering"""
    print("\n" + "="*70)
    print("CREATING DERIVED VARIABLES")
    print("="*70)

    # 1. Energy intensity flag
    print("\n1. Creating energy intensity flag...")
    energy_intensive_sectors = [
        'Petroleum products', 'Other chemicals', 'Iron and steel foundries',
        'Cement', 'Fertilizers', 'Inorganic heavy chemicals', 'Organic heavy chemicals',
        'Coal tar products', 'Synthetic fibers, resin'
    ]
    master_df['is_energy_intensive'] = master_df['io_sector_name'].isin(
        energy_intensive_sectors
    )
    print(f"  ✓ Energy-intensive observations: {master_df['is_energy_intensive'].sum():,}")

    # 2. Interaction terms
    print("\n2. Creating interaction terms...")
    if 'pagerank' in master_df.columns and 'CRUDE_PETRO_shock' in master_df.columns:
        master_df['oil_shock_x_pagerank'] = (
            master_df['CRUDE_PETRO_shock'] * master_df['pagerank']
        )
        print("  ✓ Created oil_shock_x_pagerank")

    if 'betweenness_centrality' in master_df.columns and 'CRUDE_PETRO_shock' in master_df.columns:
        master_df['oil_shock_x_betweenness'] = (
            master_df['CRUDE_PETRO_shock'] * master_df['betweenness_centrality']
        )
        print("  ✓ Created oil_shock_x_betweenness")

    # 3. Lagged variables
    print("\n3. Creating lagged variables...")
    master_df = master_df.sort_values(['io_sector_name', 'date'])

    # Lag commodity prices
    commodity_price_cols = ['CRUDE_PETRO', 'WHEAT_US_HRW', 'RICE_05', 'COPPER', 'ALUMINUM']
    commodity_price_cols = [c for c in commodity_price_cols if c in master_df.columns]

    for col in commodity_price_cols:
        master_df[f'{col}_lag1'] = master_df.groupby('io_sector_name')[col].shift(1)

    print(f"  ✓ Lagged {len(commodity_price_cols)} commodity prices")

    # Lag IIP growth
    if 'iip_yoy_growth' in master_df.columns:
        master_df['iip_yoy_growth_lag1'] = master_df.groupby(
            'io_sector_name'
        )['iip_yoy_growth'].shift(1)
        print("  ✓ Lagged IIP year-over-year growth")

    # 4. Time indicators
    print("\n4. Creating time indicators...")
    master_df['year'] = master_df['date'].dt.year
    master_df['month'] = master_df['date'].dt.month
    master_df['quarter'] = master_df['date'].dt.quarter
    print("  ✓ Added year, month, quarter")

    return master_df


def quality_checks(master_df: pd.DataFrame):
    """Perform data quality checks"""
    print("\n" + "="*70)
    print("DATA QUALITY CHECKS")
    print("="*70)

    print(f"\nFinal dataset shape: {master_df.shape[0]:,} rows × {master_df.shape[1]} columns")
    print(f"Date range: {master_df['date'].min()} to {master_df['date'].max()}")
    print(f"Unique sectors: {master_df['io_sector_name'].nunique()}")
    print(f"Unique months: {master_df['date'].nunique()}")

    # Missing values in key columns
    print("\nMissing values in key columns:")
    key_cols = ['iip_index', 'iip_yoy_growth', 'CRUDE_PETRO', 'pagerank',
                'backward_linkage', 'gdp_growth_yoy']

    for col in key_cols:
        if col in master_df.columns:
            missing_count = master_df[col].isna().sum()
            missing_pct = (missing_count / len(master_df)) * 100
            print(f"  {col:20} {missing_count:>6,} ({missing_pct:>5.2f}%)")

    # Column categories
    print("\nColumn categories:")
    col_categories = {
        'Identifiers': len([c for c in master_df.columns if any(
            x in c.lower() for x in ['sector', 'date', 'year', 'month', 'quarter']
        )]),
        'IIP variables': len([c for c in master_df.columns if 'iip' in c.lower()]),
        'Commodity prices': len([c for c in master_df.columns if any(
            x in c for x in ['CRUDE', 'WHEAT', 'RICE', 'COPPER', 'ALUMINUM']
        )]),
        'Network metrics': len([c for c in master_df.columns if any(
            x in c.lower() for x in ['linkage', 'centrality', 'pagerank']
        )]),
        'Macro variables': len([c for c in master_df.columns if any(
            x in c.lower() for x in ['gdp', 'wpi', 'oni', 'g20']
        )]),
        'Trade variables': len([c for c in master_df.columns if 'trade' in c.lower()]),
    }

    for category, count in col_categories.items():
        print(f"  {category:20} {count:3} columns")

    print(f"\n  {'TOTAL':20} {master_df.shape[1]:3} columns")


def save_datasets(master_df: pd.DataFrame):
    """Save master dataset and metadata"""
    print("\n" + "="*70)
    print("SAVING DATASETS")
    print("="*70)

    # 1. Save full dataset
    output_path = PROCESSED_DIR / 'master_dataset.csv'
    master_df.to_csv(output_path, index=False)
    print(f"\n✓ Saved full dataset: {output_path}")
    print(f"  {master_df.shape[0]:,} rows × {master_df.shape[1]} columns")

    # 2. Save filtered dataset (2010-2024, non-missing IIP)
    master_filtered = master_df[
        (master_df['date'] >= '2010-01-01') &
        (master_df['date'] <= '2024-12-31') &
        (master_df['iip_index'].notna())
    ].copy()

    filtered_path = PROCESSED_DIR / 'master_dataset_filtered.csv'
    master_filtered.to_csv(filtered_path, index=False)
    print(f"\n✓ Saved filtered dataset: {filtered_path}")
    print(f"  {master_filtered.shape[0]:,} rows × {master_filtered.shape[1]} columns")
    print(f"  Removed {len(master_df) - len(master_filtered):,} rows")

    # 3. Save column metadata
    columns_df = pd.DataFrame({
        'column_name': master_df.columns,
        'dtype': master_df.dtypes.astype(str),
        'non_null_count': master_df.count(),
        'null_count': master_df.isna().sum(),
        'null_percentage': (master_df.isna().sum() / len(master_df) * 100).round(2)
    })

    columns_path = PROCESSED_DIR / 'master_dataset_columns.csv'
    columns_df.to_csv(columns_path, index=False)
    print(f"\n✓ Saved column metadata: {columns_path}")


def main():
    """Run complete master dataset creation pipeline"""
    print("="*70)
    print("MASTER DATASET CREATION PIPELINE")
    print("="*70)

    # Step 1: Load all datasets
    datasets = load_all_datasets()

    # Step 2: Create sector mapping
    sector_mapping = create_sector_mapping()

    # Step 3: Merge all datasets
    master_df = merge_datasets(datasets, sector_mapping)

    # Step 4: Create derived variables
    master_df = create_derived_variables(master_df)

    # Step 5: Quality checks
    quality_checks(master_df)

    # Step 6: Save datasets
    save_datasets(master_df)

    print("\n" + "="*70)
    print("MASTER DATASET CREATION COMPLETE!")
    print("="*70)
    print(f"\nAll files saved to: {PROCESSED_DIR}")


if __name__ == "__main__":
    main()
