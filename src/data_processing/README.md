# Data Processing Scripts

This directory contains Python scripts for processing raw data into analysis-ready datasets. These scripts are derived from the Jupyter notebooks in the `notebooks/` directory.

## Scripts

### 1. `clean_data.py`
Cleans and processes multiple data sources from raw format to processed CSV files.

**Data sources processed:**
- Commodity prices (CMO monthly data)
- Climate data (ONI - Oceanic Nino Index)
- Trade data (bilateral trade flows)
- Country mapping (ISO3 codes and regions)
- IIP (Index of Industrial Production)
- WPI (Wholesale Price Index)
- GDP (quarterly estimates)
- OECD global macro data

**Usage:**
```bash
python src/data_processing/clean_data.py
```

**Outputs:**
- `data/processed/proc_cmo_monthly.csv` - Commodity prices with log returns, volatility, and shocks
- `data/processed/climate_oni_clean.csv` - Climate indices with ENSO phases and lags
- `data/processed/trade_india_bilateral.csv` - Bilateral trade flows
- `data/processed/country_mapping.csv` - Country ISO3 codes and regions
- `data/processed/iip_sectoral.csv` - Sectoral industrial production indices
- `data/processed/wpi_inflation.csv` - Wholesale price inflation
- `data/processed/gdp_quarterly.csv` - GDP with growth rates
- `data/processed/global_macro.csv` - OECD CPI data

**Based on notebook:** `notebooks/data_cleaning.ipynb`

---

### 2. `create_master_dataset.py`
Merges all processed datasets into a single master dataset for analysis.

**Features:**
- Sector mapping from IIP to I-O sectors
- Time-series alignment across all data sources
- Derived variables and feature engineering
- Lagged variables for econometric analysis
- Energy intensity flags and interaction terms

**Usage:**
```bash
python src/data_processing/create_master_dataset.py
```

**Outputs:**
- `data/processed/master_dataset.csv` - Full master dataset
- `data/processed/master_dataset_filtered.csv` - Filtered for 2010-2024, non-missing IIP
- `data/processed/master_dataset_columns.csv` - Column metadata and missing value statistics

**Based on notebook:** `notebooks/create_master_dataset.ipynb`

---

## Network Analysis Script

### `src/network_analysis/process_io_table.py`
Processes Input-Output tables to calculate network metrics.

**Calculations:**
- Technical coefficients matrix (A = input/output)
- Leontief inverse matrix (L = (I-A)^-1)
- Backward and forward linkages
- Network centrality metrics (PageRank, betweenness, degree, etc.)
- Production network edges

**Usage:**
```bash
python src/network_analysis/process_io_table.py
```

**Outputs:**
- `data/processed_io_data/technical_coefficients.csv`
- `data/processed_io_data/leontief_inverse.csv`
- `data/processed_io_data/production_network_nodes.csv`
- `data/processed_io_data/production_network_edges.csv`
- `data/processed_io_data/network_metrics.csv`

**Based on notebook:** `notebooks/iotable_processing.ipynb`

---

## Data Flow

```
Raw Data (data/raw/)
    ↓
clean_data.py
    ↓
Processed Data (data/processed/)
    ↓
create_master_dataset.py
    ↓
Master Dataset (data/processed/master_dataset.csv)

Raw I-O Tables (data/processed/MOSPI Matrix Final - ALL.csv)
    ↓
process_io_table.py
    ↓
Network Metrics (data/processed_io_data/)
    ↓
(merged into master dataset)
```

---

## Data Dictionary

### Master Dataset Key Variables

**Identifiers:**
- `date` - Month (YYYY-MM-DD)
- `sector_name` - IIP sector name
- `io_sector_name` - Mapped I-O sector name
- `sector_id` - I-O sector ID

**Production Variables:**
- `iip_index` - Industrial Production Index (base 2011-12=100)
- `iip_mom_growth` - Month-over-month growth (%)
- `iip_yoy_growth` - Year-over-year growth (%)

**Network Metrics:**
- `backward_linkage` - Total backward linkage (sum of column in Leontief matrix)
- `forward_linkage` - Total forward linkage (sum of row in Leontief matrix)
- `pagerank` - PageRank centrality
- `betweenness_centrality` - Betweenness centrality
- `degree_centrality` - Degree centrality
- `is_key_sector` - Binary flag for key sectors (high backward + forward linkages)

**Commodity Prices:**
- `CRUDE_PETRO` - Crude oil price ($/barrel)
- `WHEAT_US_HRW` - Wheat price ($/MT)
- `RICE_05` - Rice price ($/MT)
- `COPPER` - Copper price ($/MT)
- `ALUMINUM` - Aluminum price ($/MT)
- `*_logret` - Log returns
- `*_vol_3m/6m/12m` - Rolling volatility
- `*_shock` - Binary shock indicator (>2 std dev)

**Climate Variables:**
- `ONI` - Oceanic Nino Index
- `ENSO_Phase` - El Nino/La Nina/Neutral
- `ONI_lag_1m/3m/6m` - Lagged ONI values

**Macro Variables:**
- `gdp_constant` - Real GDP
- `gdp_current` - Nominal GDP
- `gdp_growth_yoy` - GDP growth rate (%)
- `wpi_*` - Wholesale price inflation by category
- `g20_avg_cpi_growth` - G20 average CPI growth

**Trade Variables:**
- `total_trade_value` - Total bilateral trade (USD)
- `energy_trade_value` - Energy commodity trade (USD)

**Derived Variables:**
- `is_energy_intensive` - Binary flag for energy-intensive sectors
- `oil_shock_x_pagerank` - Interaction term
- `oil_shock_x_betweenness` - Interaction term
- `*_lag1` - One-month lagged values
- `year`, `month`, `quarter` - Time indicators

---

## Requirements

See `requirements.txt` for package dependencies:
- pandas
- numpy
- polars
- networkx
- pycountry
- pycountry-convert
- openpyxl

---

## Notes

- All scripts assume they are run from the project root directory
- Processed data is gitignored; run scripts to regenerate
- Notebooks contain exploratory analysis and visualization
- Scripts are production-ready versions of notebook code
