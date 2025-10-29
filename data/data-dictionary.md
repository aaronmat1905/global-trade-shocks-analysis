# Data Dictionary - Global Trade Shocks Analysis

## Overview
This document describes all datasets for the **Global Commodity Shocks & Production Networks** project, including data sources, processing methods, and variable definitions.

**Last Updated:** 2025-10-29
**Master Dataset:** `data/processed/master_dataset.csv`
**Dimensions:** 3,476 rows × 93 columns (2012-2024, 22 manufacturing sectors)

---

## Table of Contents
1. [Raw Data Sources](#raw-data-sources)
2. [Processed Datasets](#processed-datasets)
3. [Master Dataset Variables](#master-dataset-variables)
4. [Network Metrics](#network-metrics)
5. [Data Processing Scripts](#data-processing-scripts)

---

## Raw Data Sources

### 1. Commodity Prices
**File:** `data/raw/CMO-Historical-Data-Monthly.xlsx`
**Source:** World Bank Pink Sheet (Commodity Markets)
**URL:** https://www.worldbank.org/en/research/commodity-markets
**Coverage:** Monthly, 1960-2024
**Variables:** 70+ commodity prices (energy, agriculture, metals)

**Key Commodities Used:**
- Energy: Crude oil (average of Brent, WTI, Dubai)
- Agriculture: Wheat (US HRW), Rice (Thai 5%)
- Metals: Copper, Aluminum

**Processing:** `src/data_processing/clean_data.py::clean_commodity_prices()`
**Output:** `data/processed/proc_cmo_monthly.csv`

---

### 2. Climate Data (Instrumental Variable)
**File:** Downloaded from NOAA API
**Source:** NOAA Climate Prediction Center - Oceanic Niño Index
**URL:** https://www.cpc.ncep.noaa.gov/data/indices/
**Coverage:** Monthly, 1950-2024
**Variable:** ONI (3-month running mean SST anomaly in Niño 3.4 region)

**Purpose:** Instrumental variable for agricultural commodity prices in causal analysis

**Processing:** `src/data_processing/clean_data.py::clean_climate_data()`
**Output:** `data/processed/climate_oni_clean.csv`

---

### 3. Bilateral Trade Data
**File:** `data/raw/IMTSTrade.csv` (3 GB)
**Source:** IMF International Merchandise Trade Statistics (IMTS)
**URL:** https://data.imf.org/?sk=9D6028D4-F14A-464C-A2F2-59B2CD424B85
**Coverage:** Monthly bilateral trade flows, all countries, 2000-2024

**Trade Partners (8 selected):** USA, China, Saudi Arabia, UAE, Qatar, Germany, France, Italy

**Commodity Groups (HS Classification):**
- Energy (HS 27): Mineral fuels, oils
- Food (HS 10, 11): Cereals, grain products
- Metals (HS 74, 76): Copper, Aluminum

**Processing:** `src/data_processing/clean_data.py::clean_trade_data()`
**Output:** `data/processed/trade_india_bilateral.csv`

**Auxiliary File:** `data/raw/WITS-Partner.xlsx` - Country mapping (ISO3 codes, regions)
**Output:** `data/processed/country_mapping.csv`

---

### 4. Industrial Production Data
**File:** `data/raw/IndexofIndustrialProduction.xlsx`
**Source:** Reserve Bank of India (RBI) / MOSPI
**URL:** https://rbi.org.in/Scripts/AnnualPublications.aspx
**Coverage:** Monthly, 2011-2024, Base year 2011-12=100

**Sectors (22 manufacturing sectors used):**
- Food products
- Beverages
- Textiles
- Wearing apparel
- Leather products
- Paper products
- Printing & publishing
- Chemicals
- Pharmaceuticals
- Petroleum products
- Rubber & plastics
- Non-metallic minerals
- Basic metals
- Fabricated metal products
- Machinery & equipment
- Computer & electronics
- Electrical equipment
- Motor vehicles
- Other transport equipment
- Furniture
- Tobacco products
- Other manufacturing

**Processing:** `src/data_processing/clean_data.py::clean_iip_data()`
**Output:** `data/processed/iip_sectoral.csv`

---

### 5. Wholesale Price Index
**File:** `data/raw/WholesalePriceIndexMonthlyData.xlsx`
**Source:** Office of Economic Adviser, Ministry of Commerce, India
**Coverage:** Monthly, 2011-2024, Base year 2011-12=100

**Categories Used:**
- Fuel & Power
- Manufactured Products
- Food Articles

**Processing:** `src/data_processing/clean_data.py::clean_wpi_data()`
**Output:** `data/processed/wpi_inflation.csv`

---

### 6. GDP Data
**Files:**
- `data/raw/GDP_Constant.xlsx` (Real GDP)
- `data/raw/GDP_Current.xlsx` (Nominal GDP)
- `data/raw/GVA_Current.xlsx` (Gross Value Added by sector)

**Source:** MOSPI National Accounts Statistics
**Coverage:** Quarterly, 2011-2024, Base year 2011-12

**Processing:** `src/data_processing/clean_data.py::clean_gdp_data()`
**Output:** `data/processed/gdp_quarterly.csv` (resampled to monthly)

---

### 7. Global Macroeconomic Data
**File:** `data/raw/OECD_file.csv`
**Source:** OECD Statistics
**URL:** https://stats.oecd.org/
**Coverage:** G20 countries, monthly CPI growth

**Processing:** `src/data_processing/clean_data.py::clean_oecd_data()`
**Output:** `data/processed/global_macro.csv`

---

### 8. Input-Output Tables
**File:** `data/processed/MOSPI Matrix Final - ALL.csv`
**Source:** MOSPI (Ministry of Statistics & Programme Implementation)
**Year:** 2015-16
**Dimensions:** 131 sectors × 131 sectors

**Use Table Structure:**
- Rows: Producing sectors (supply inputs)
- Columns: Consuming sectors (use inputs)
- Cell (i,j): Rupees worth of inputs from sector i used by sector j

**Processing:** `src/network_analysis/process_io_table.py`
**Outputs:**
- `data/processed_io_data/technical_coefficients.csv`
- `data/processed_io_data/leontief_inverse.csv`
- `data/processed_io_data/production_network_nodes.csv`
- `data/processed_io_data/production_network_edges.csv`
- `data/processed_io_data/network_metrics.csv`

---

## Processed Datasets

### Master Dataset
**File:** `data/processed/master_dataset.csv`
**Dimensions:** 3,476 rows × 93 columns
**Time Range:** April 2012 - December 2024 (153 months)
**Sectors:** 22 manufacturing sectors (mapped from IIP to I-O classification)

**Filtered Version:** `data/processed/master_dataset_filtered.csv` (same dimensions, quality-filtered)

**Metadata:** `data/processed/master_dataset_columns.csv` (column-level missing value stats)

---

## Master Dataset Variables

### Identifiers (5 variables)
| Variable | Type | Description |
|----------|------|-------------|
| `date` | datetime | Month (YYYY-MM-01) |
| `sector_name` | string | IIP sector name |
| `io_sector_name` | string | Mapped I-O sector name (131 sectors) |
| `sector_id` | int | I-O sector ID (1-131) |
| `year`, `month`, `quarter` | int | Time indicators |

### Production Variables (4 variables)
| Variable | Type | Description | Source |
|----------|------|-------------|--------|
| `iip_index` | float | Industrial Production Index (2011-12=100) | RBI IIP |
| `iip_mom_growth` | float | Month-over-month growth (%) | Calculated |
| `iip_yoy_growth` | float | Year-over-year growth (%) | Calculated |
| `is_energy_intensive` | bool | Energy-intensive sector flag | Classification |

### Network Metrics (8 variables)
| Variable | Type | Description | Calculation |
|----------|------|-------------|-------------|
| `backward_linkage` | float | Total backward linkage (demand pull) | Sum of Leontief column |
| `forward_linkage` | float | Total forward linkage (supply push) | Sum of Leontief row |
| `is_key_sector` | bool | High backward + forward linkage | Both > average |
| `degree_centrality` | float | Network degree centrality | NetworkX |
| `betweenness_centrality` | float | Betweenness centrality (bottleneck measure) | NetworkX |
| `closeness_centrality` | float | Closeness centrality | NetworkX |
| `eigenvector_centrality` | float | Eigenvector centrality | NetworkX |
| `pagerank` | float | PageRank score | NetworkX |

### Commodity Prices (35 variables)

**Level Variables (5):**
- `CRUDE_PETRO` - Crude oil price ($/barrel)
- `WHEAT_US_HRW` - Wheat price ($/MT)
- `RICE_05` - Rice price ($/MT)
- `COPPER` - Copper price ($/MT)
- `ALUMINUM` - Aluminum price ($/MT)

**Log Returns (5):**
- `{COMMODITY}_logret` - Log returns: ln(P_t / P_{t-1})

**Rolling Volatility (15):**
- `{COMMODITY}_vol_3m` - 3-month rolling standard deviation of log returns
- `{COMMODITY}_vol_6m` - 6-month rolling standard deviation
- `{COMMODITY}_vol_12m` - 12-month rolling standard deviation

**Shock Indicators (5):**
- `{COMMODITY}_shock` - Binary: 1 if |log return| > 2 std deviations

**Lagged Prices (5):**
- `{COMMODITY}_lag1` - 1-month lagged price

### Climate Variables (6 variables)
| Variable | Type | Description |
|----------|------|-------------|
| `ONI` | float | Oceanic Niño Index (°C anomaly) |
| `ENSO_Phase` | string | El Niño / La Niña / Neutral |
| `ONI_lag_1m` | float | ONI lagged 1 month |
| `ONI_lag_3m` | float | ONI lagged 3 months |
| `ONI_lag_6m` | float | ONI lagged 6 months |
| `Year`, `Month`, `Month_num` | int | Time indicators from climate data |

### Macroeconomic Variables (11 variables)

**GDP (3):**
- `gdp_constant` - Real GDP (₹ crores, 2011-12 prices)
- `gdp_current` - Nominal GDP (₹ crores, current prices)
- `gdp_growth_yoy` - Real GDP YoY growth (%)

**WPI Inflation (3):**
- `wpi_(a)__food_articles` - Food articles WPI YoY inflation (%)
- `wpi_ii_fuel_and_power` - Fuel & power WPI YoY inflation (%)
- `wpi_iii___manufactured_products` - Manufactured products WPI YoY inflation (%)

**Global Macro (18 country-level + 1 aggregate):**
- `ARG`, `AUS`, `BRA`, `CAN`, `CHN`, `DEU`, `EA20`, `EU27_2020`, `FRA`, `GBR`, `IDN`, `IND`, `ITA`, `KOR`, `SAU`, `TUR`, `USA`, `ZAF` - Country CPI YoY growth (%)
- `g20_avg_cpi_growth` - G20 average CPI growth (%) [Currently sparse: 97% missing]

### Trade Variables (2 variables)
| Variable | Type | Description |
|----------|------|-------------|
| `energy_trade_value` | float | Energy commodity trade value (USD) |
| `total_trade_value` | float | Total bilateral trade value (USD) |

### Derived Variables (7 variables)
| Variable | Type | Description |
|----------|------|-------------|
| `is_energy_intensive` | bool | Energy-intensive sector classification |
| `oil_shock_x_pagerank` | float | Interaction: oil shock × PageRank |
| `oil_shock_x_betweenness` | float | Interaction: oil shock × betweenness |
| `iip_yoy_growth_lag1` | float | Lagged IIP YoY growth (1 month) |
| `year`, `month`, `quarter` | int | Time indicators |

---

## Network Metrics

### Technical Coefficients Matrix
**File:** `data/processed_io_data/technical_coefficients.csv`
**Dimensions:** 131 sectors × 131 sectors
**Formula:** `a_ij = input_ij / total_output_j`
**Interpretation:** Rupees of input from sector i needed to produce 1 rupee of output in sector j

### Leontief Inverse Matrix
**File:** `data/processed_io_data/leontief_inverse.csv`
**Dimensions:** 131 sectors × 131 sectors
**Formula:** `L = (I - A)^{-1}` where A is technical coefficients, I is identity
**Interpretation:** Total (direct + indirect) output from sector i needed to satisfy 1 unit of final demand in sector j

### Production Network Nodes
**File:** `data/processed_io_data/production_network_nodes.csv`
**Rows:** 131 sectors

**Variables:**
- `sector_id` - Unique sector ID (1-131)
- `sector_name` - Sector name
- `backward_linkage` - Sum of Leontief column (demand-side linkage)
- `forward_linkage` - Sum of Leontief row (supply-side linkage)
- `is_key_sector` - Both linkages > average
- `degree_centrality` - Normalized degree centrality
- `betweenness_centrality` - Fraction of shortest paths through this sector
- `closeness_centrality` - Inverse average distance to all sectors
- `eigenvector_centrality` - Importance based on neighbors' importance
- `pagerank` - PageRank score

**Key Sectors (11 identified):**
Sectors with both backward linkage > 2.50 AND forward linkage > 2.50

**Top Sectors by PageRank:**
1. Bicycles, cycle-rickshaw (0.0499)
2. Tobacco Products (0.0453)
3. Public administration (0.0171)

**Top Bridge Sectors (Betweenness):**
1. Trade (0.1357)
2. Construction services (0.0484)
3. Miscellaneous food products (0.0351)

### Production Network Edges
**File:** `data/processed_io_data/production_network_edges.csv`
**Rows:** 3,401 edges (filtered: coefficient > 0.001)

**Variables:**
- `source_sector` - Supplying sector name
- `target_sector` - Receiving sector name
- `input_coefficient` - Technical coefficient a_ij
- `input_value` - Value of input flow (₹ crores)

**Network Statistics:**
- Nodes: 131
- Edges: 3,401
- Density: 19.82%
- Direction: Directed (supplier → user)

---

## Data Processing Scripts

### Complete Processing Pipeline

```bash
# Step 1: Clean all raw data sources
python src/data_processing/clean_data.py
```
**Outputs:**
- `data/processed/proc_cmo_monthly.csv`
- `data/processed/climate_oni_clean.csv`
- `data/processed/trade_india_bilateral.csv`
- `data/processed/country_mapping.csv`
- `data/processed/iip_sectoral.csv`
- `data/processed/wpi_inflation.csv`
- `data/processed/gdp_quarterly.csv`
- `data/processed/global_macro.csv`

```bash
# Step 2: Process I-O tables and calculate network metrics
python src/network_analysis/process_io_table.py
```
**Outputs:**
- `data/processed_io_data/technical_coefficients.csv`
- `data/processed_io_data/leontief_inverse.csv`
- `data/processed_io_data/production_network_nodes.csv`
- `data/processed_io_data/production_network_edges.csv`
- `data/processed_io_data/network_metrics.csv`

```bash
# Step 3: Create master dataset
python src/data_processing/create_master_dataset.py
```
**Outputs:**
- `data/processed/master_dataset.csv`
- `data/processed/master_dataset_filtered.csv`
- `data/processed/master_dataset_columns.csv`

### Sector Mapping (IIP to I-O)

22 IIP manufacturing sectors mapped to 131 I-O sectors:

| IIP Sector | I-O Sector |
|------------|------------|
| Manufacture of food products | Miscellaneous food products |
| Manufacture of beverages | Beverages |
| Manufacture of textiles | Cotton textiles |
| Manufacture of wearing apparel | Ready made garments |
| Manufacture of leather and related products | Leather and leather products |
| Manufacture of paper and paper products | Paper, Paper products and newsprint |
| Printing and reproduction of recorded media | Publishing, printing and allied activities |
| Manufacture of chemicals and chemical products | Other chemicals |
| Manufacture of pharmaceuticals... | Drugs and medicine |
| Manufacture of coke and refined petroleum products | Petroleum products |
| Manufacture of rubber and plastics products | Plastic products |
| Manufacture of other non-metallic mineral products | Cement |
| Manufacture of basic metals | Iron and steel foundries |
| Manufacture of fabricated metal products... | Miscellaneous metal products |
| Manufacture of machinery and equipment n.e.c. | Other non-electrical machinery |
| Manufacture of computer, electronic and optical products | Electronic equipments(incl.TV) |
| Manufacture of electrical equipment | Electrical industrial Machinery |
| Manufacture of motor vehicles, trailers... | Motor vehicles |
| Manufacture of other transport equipment | Other transport equipments |
| Manufacture of furniture | Furniture & Fixtures |
| Manufacture of tobacco products | Tobacco Products |
| Other manufacturing | Miscellaneous manufacturing |

---

## Data Quality Notes

### Missing Values in Master Dataset

**High missingness (>90%):**
- `g20_avg_cpi_growth` (97.5%) - OECD data only available 2024-09 onwards

**Moderate missingness (10-30%):**
- `gdp_growth_yoy` (29.8%) - First 12 months have no YoY comparison
- `iip_yoy_growth` (8.2%) - First 12 months have no YoY comparison

**Low missingness (<5%):**
- All commodity prices (0%)
- All network metrics (0%)
- IIP index (0%)

### Time Coverage

**Full coverage:** 2012-04 to 2024-12
- Commodity prices: 2010-01 to 2024-12 (180 months)
- IIP data: 2012-04 to 2024-12 (153 months) **← Master dataset range**
- Network metrics: Static (2015-16 I-O table)
- Climate data: 2010-01 to 2017-11 (96 months) **⚠️ Limited coverage**

### Known Limitations

1. **Climate data (ONI):** Stops at 2017-11, need to update with latest NOAA data
2. **I-O table:** Uses 2015-16 table; sector structure may have changed
3. **Trade data:** 3GB file requires chunking/filtering during processing
4. **G20 macro data:** Very limited time coverage in current dataset

---

## References

**Data Sources:**
- World Bank Pink Sheet: https://www.worldbank.org/en/research/commodity-markets
- NOAA ONI: https://www.cpc.ncep.noaa.gov/data/indices/
- IMF IMTS: https://data.imf.org/?sk=9D6028D4-F14A-464C-A2F2-59B2CD424B85
- RBI Database: https://rbi.org.in/Scripts/AnnualPublications.aspx
- MOSPI: http://mospi.nic.in/
- OECD Statistics: https://stats.oecd.org/

**Methodology:**
- Leontief Input-Output Model: Leontief, W. (1936). "Quantitative Input-Output Relations in the Economic System of the United States"
- Network Centrality Measures: Newman, M. E. J. (2010). "Networks: An Introduction"

---

**Document Version:** 2.0
**Last Updated:** 2025-10-29
**Maintained By:** Project Team

For processing code details, see [src/data_processing/README.md](../src/data_processing/README.md)
