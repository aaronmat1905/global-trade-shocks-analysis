# Project Data Dictionary & Processing Guide

## Overview
This document describes all datasets for the **Global Commodity Shocks & Production Networks** project. Each team member should process their assigned datasets following the specifications below.

---

## 1. COMMODITY PRICES DATA

### **File:** `CMO-Historical-Data-Monthly.xlsx`
**Location:** `data/raw/commodity_prices/`  
**Source:** World Bank Pink Sheet  
**Coverage:** Monthly, 1960-2024  

#### **What It Contains:**
- **Sheet 1 - Monthly Prices:** Nominal prices (USD) for 70+ commodities
  - Energy: Crude oil (Brent, WTI, Dubai), Natural gas, Coal
  - Agriculture: Wheat, Rice, Maize, Soybeans, Sugar, Coffee
  - Metals: Copper, Aluminum, Iron ore, Gold, Silver
  
- **Sheet 2 - Monthly Indices:** Price indices (2010=100 base year)
  - Aggregate indices by commodity group
  - Useful for comparing relative price movements

- **Sheet 3 - Index Weights:** Weights used in index construction

#### **Why We Need It:**
This is our **primary shock variable**. Oil price spikes, wheat price volatility, and metal price crashes are the "shocks" we're studying. Changes in these prices affect India's production network.

#### **Processing Tasks:**
1. Extract columns: Date, Crude oil (average), Wheat (US HRW), Rice (Thai 5%), Copper, Aluminum
2. Filter to 2010-2024 only
3. Calculate log returns: `log(Price_t / Price_{t-1})`
4. Calculate rolling volatility (3, 6, 12-month windows)
5. Create shock indicators: binary variable = 1 if price change > 2 standard deviations
6. Save as: `data/processed/commodity_prices_clean.csv`

#### **Expected Output Columns:**
```
date, oil_price, wheat_price, rice_price, copper_price, aluminum_price,
oil_return, wheat_return, rice_return, copper_return, aluminum_return,
oil_volatility_3m, oil_volatility_6m, oil_volatility_12m,
oil_shock_binary, wheat_shock_binary, etc.
```

---

## 2. CLIMATE DATA (INSTRUMENTAL VARIABLE)

### **File:** `Monthly Oceanic Nino Index (ONI) - Wide.csv`
**Location:** `data/raw/climate/`  
**Source:** NOAA Climate Prediction Center  
**Coverage:** Monthly, 1950-2024  

#### **What It Contains:**
- **Oceanic Niño Index (ONI):** 3-month running mean of sea surface temperature anomalies in the Niño 3.4 region
- Values range from -2.5°C (strong La Niña) to +2.5°C (strong El Niño)

#### **Why We Need It:**
El Niño/La Niña events affect global weather patterns → agricultural production → wheat/rice prices. We use ONI as an **instrumental variable** (IV) for agricultural commodity prices because:
- ONI affects crop yields (relevant)
- ONI doesn't directly affect Indian manufacturing output (excludable)
- This helps us establish **causal** relationships, not just correlations

#### **Processing Tasks:**
1. Filter to 2010-2024
2. Classify ENSO phases:
   - El Niño: ONI ≥ 0.5
   - La Niña: ONI ≤ -0.5
   - Neutral: -0.5 < ONI < 0.5
3. Create lag variables (1, 3, 6 months) - weather affects crops with delay
4. Save as: `data/processed/climate_oni_clean.csv`

#### **Expected Output Columns:**
```
date, oni_index, enso_phase, oni_lag1, oni_lag3, oni_lag6
```

---

## 3. TRADE DATA

### **File:** `dataset_2025-10-22T07_56_33...csv` (3 GB!)
**Location:** `data/raw/trade/`  
**Source:** IMF International Merchandise Trade Statistics (IMTS)  
**Coverage:** Monthly bilateral trade flows, all countries, 2000-2024  

#### **What It Contains:**
- **Bilateral trade flows:** Country A → Country B, by product category
- **Trade values:** Imports/Exports in USD
- **Product codes:** HS classification (Harmonized System)

#### **Why We Need It:**
Measures India's trade exposure to different countries and commodities. High dependence on Gulf states for oil = high vulnerability to oil shocks.

#### **Processing Tasks:**
1. **Filter to India only:** Reporter = India
2. **Select 8 key partners:** USA, China, Saudi Arabia, UAE, Qatar, Germany, France, Italy
3. **Aggregate by commodity group:**
   - Energy (HS 27): Mineral fuels, oils
   - Food (HS 10, 11): Cereals, grain products
   - Metals (HS 74, 76): Copper, Aluminum
4. Calculate trade concentration metrics:
   - **HHI (Herfindahl Index):** Sum of squared trade shares
   - Partner diversification score
5. Save as: `data/processed/trade_india_bilateral.csv`

#### **Expected Output Columns:**
```
date, partner_country, commodity_group, 
import_value_usd, export_value_usd, trade_balance,
import_share, export_share
```

#### **Warning:** This file is HUGE (3GB). Use `pd.read_csv(chunksize=100000)` or filter early with SQL/Dask.

---

### **File:** `WITS-Partner.xlsx`
**Location:** `data/raw/trade/`  
**Source:** World Bank WITS (World Integrated Trade Solution)  
**Coverage:** Annual trade data with partner country details  

#### **What It Contains:**
- Country names, ISO codes, regional classifications
- Use as a lookup table to map country codes → country names

#### **Processing Tasks:**
1. Extract mapping: ISO3 code → Country name → Region
2. Merge with IMF trade data
3. Save as: `data/processed/country_mapping.csv`

---

## 4. MACROECONOMIC DATA

### **File:** `Index of Industrial Production.xlsx`
**Location:** `data/raw/macroeconomic/`  
**Source:** Reserve Bank of India (RBI)  
**Coverage:** Monthly, 2010-2024, Base year 2011-12  

#### **What It Contains:**
- **IIP General Index:** Overall industrial production
- **Sectoral Indices:**
  - Mining & Quarrying
  - Manufacturing (15+ sub-sectors: Food, Textiles, Chemicals, Metals, Machinery, etc.)
  - Electricity
- **Use-based Classification:**
  - Basic goods
  - Capital goods
  - Intermediate goods
  - Consumer durables
  - Consumer non-durables

#### **Why We Need It:**
This is our **main outcome variable**. We're predicting: "When oil prices spike, which manufacturing sectors see production decline?" IIP measures exactly that.

#### **Processing Tasks:**
1. Extract all sectoral indices (rows) across time (columns)
2. Convert from wide to long format:
   ```
   date | sector | iip_value
   ```
3. Calculate month-over-month growth rates
4. Calculate year-over-year growth rates
5. Identify energy-intensive sectors (Manufacturing - Chemicals, Basic Metals, etc.)
6. Save as: `data/processed/iip_sectoral.csv`

#### **Expected Output Columns:**
```
date, sector_name, iip_index, 
iip_mom_growth, iip_yoy_growth,
is_energy_intensive
```

---

### **File:** `Wholesale Price Index - Monthly Data.xlsx`
**Location:** `data/raw/macroeconomic/`  
**Source:** Office of Economic Adviser, India  
**Coverage:** Monthly, 2010-2024  

#### **What It Contains:**
- WPI for different product categories
- Inflation measure at wholesale level (before goods reach consumers)

#### **Why We Need It:**
Commodity price shocks → input cost inflation → affects production decisions. WPI captures cost pressures on manufacturers.

#### **Processing Tasks:**
1. Extract WPI for: Fuel & Power, Manufactured Products, Food Articles
2. Calculate inflation rate: `(WPI_t - WPI_{t-12}) / WPI_{t-12} * 100`
3. Save as: `data/processed/wpi_inflation.csv`

---

### **Files:** GDP Quarterly Estimates (3 files)
**Location:** `data/raw/macroeconomic/`  
**Source:** MOSPI National Accounts Statistics  

#### **What They Contain:**
- Quarterly GDP at constant prices (real GDP)
- Quarterly GDP at current prices (nominal GDP)
- Quarterly GVA (Gross Value Added) by sector

#### **Why We Need It:**
Control variables for macroeconomic conditions. GDP growth affects all sectors simultaneously.

#### **Processing Tasks:**
1. Merge all three files
2. Calculate GDP growth rate (YoY)
3. Resample to monthly frequency (forward-fill)
4. Save as: `data/processed/gdp_quarterly.csv`

---

### **Files:** OECD Data (2 CSV files)
**Location:** `data/raw/macroeconomic/`  
**Source:** OECD Data Explorer  

#### **What They Contain:**
- **File 1:** G20 GDP growth rates (quarterly)
- **File 2:** G20 price indices (monthly)

#### **Why We Need It:**
Global economic conditions affect India through trade channels. US/China/EU slowdowns reduce demand for Indian exports.

#### **Processing Tasks:**
1. Extract data for: USA, China, Germany, France, Italy (India's trade partners)
2. Calculate average G20 GDP growth
3. Merge with India data
4. Save as: `data/processed/global_macro.csv`

---

## 5. INPUT-OUTPUT TABLE

### **File:** `Input-Output-Transactions-Table-India-2015-16.pdf`
**Location:** `data/raw/input_output/`  
**Source:** MOSPI (Ministry of Statistics, India)  
**Coverage:** 139 sectors, year 2015-16  

#### **What It Contains:**
- **Use Table:** Shows which sectors use inputs from which other sectors
  - Rows = industries producing inputs
  - Columns = industries using inputs
  - Cell (i,j) = Sector j buys inputs worth ₹X from sector i

- **Make Table:** Shows which sectors produce which outputs
  - Rows = industries
  - Columns = products
  - Cell (i,j) = Sector i produces ₹X worth of product j

#### **Why We Need It:**
This is the **CORE** of the project. The I-O table shows the **production network**:
- Oil refining → Chemicals → Plastics → Manufacturing
- If oil prices spike → refining costs up → chemicals cost up → plastics cost up → manufacturing slows

We model these cascading effects through the network structure.

#### **Processing Tasks:**
**WARNING:** This is a PDF with large tables. Need careful extraction.

1. **Extract Use Table:**
   - Use Tabula or pdfplumber to extract tables
   - Create 139×139 matrix: `A[i,j]` = input from sector i to sector j
   
2. **Calculate Technical Coefficients:**
   - `a[i,j] = A[i,j] / X[j]` where X[j] = total output of sector j
   - This gives "input per unit of output"
   
3. **Calculate Leontief Inverse:**
   - `L = (I - a)^(-1)` where I is identity matrix
   - L[i,j] = total output from sector i needed to produce 1 unit of final demand in sector j
   - This captures **direct + indirect** linkages
   
4. **Calculate Forward & Backward Linkages:**
   - Backward linkage = sum of column in L matrix (how much sector j pulls from others)
   - Forward linkage = sum of row in L matrix (how much sector i pushes to others)
   
5. **Build Network Graph:**
   - Nodes = 139 sectors
   - Edge (i→j) with weight = a[i,j] (technical coefficient)
   - Save edge list as: `data/processed/production_network_edges.csv`
   - Save node attributes as: `data/processed/production_network_nodes.csv`

#### **Expected Outputs:**
```
production_network_edges.csv:
source_sector, target_sector, input_coefficient, input_value

production_network_nodes.csv:
sector_id, sector_name, 
backward_linkage, forward_linkage,
total_output, is_key_sector
```

---

## 6. NETWORK METRICS TO CALCULATE

Once production network is built, calculate these for each sector:

### **Centrality Measures:**
1. **Degree Centrality:**
   - In-degree: How many sectors provide inputs to this sector
   - Out-degree: How many sectors does this sector supply to
   
2. **Betweenness Centrality:**
   - How often this sector lies on shortest paths between other sectors
   - High betweenness = bottleneck sector (e.g., electricity, transport)
   
3. **Closeness Centrality:**
   - Average distance to all other sectors
   - High closeness = well-connected, quickly affected by shocks
   
4. **Eigenvector Centrality:**
   - Importance based on importance of neighbors
   - High eigenvector = connected to other important sectors
   
5. **PageRank:**
   - Google's algorithm applied to production network
   - Measures "influence" in the network

### **Network Topology:**
1. **Clustering Coefficient:** How interconnected are neighbors
2. **Path Length:** Average steps between any two sectors
3. **Network Density:** % of possible connections that exist
4. **Community Detection:** Groups of tightly connected sectors

**Save as:** `data/processed/network_metrics.csv`

---

## SUMMARY: TEAM TASK ASSIGNMENTS

### **Person 1: Commodity Prices + Climate**
- Process CMO commodity prices
- Process NOAA ONI climate data
- Create shock indicators
- **Deliverable:** `commodity_prices_clean.csv`, `climate_oni_clean.csv`

### **Person 2: Trade Data**
- Process IMF IMTS (3GB file - use chunking!)
- Calculate trade concentration indices
- Merge with country mapping
- **Deliverable:** `trade_india_bilateral.csv`, `trade_concentration.csv`

### **Person 3: Macroeconomic Data**
- Process IIP (most important!)
- Process WPI, CPI, GDP files
- Merge OECD global data
- **Deliverable:** `iip_sectoral.csv`, `macro_controls.csv`

### **Person 4: Input-Output Table + Network**
- Extract I-O table from PDF (hardest task!)
- Build production network
- Calculate Leontief inverse
- Calculate all network metrics
- **Deliverable:** `production_network_edges.csv`, `production_network_nodes.csv`, `network_metrics.csv`

---

## FINAL MERGED DATASET

Once all processing is complete, merge into master dataset:

**File:** `data/processed/master_dataset.csv`

**Structure:**
```
date, sector_name,
oil_price, wheat_price, copper_price, aluminum_price,
oil_shock, wheat_shock,
oni_index, enso_phase,
import_value, export_value, trade_hhi,
iip_index, iip_growth,
wpi_inflation, gdp_growth,
degree_centrality, betweenness_centrality, eigenvector_centrality,
backward_linkage, forward_linkage,
is_energy_intensive, is_key_sector
```

**Dimensions:** ~180 months × 139 sectors × 30+ features = ~750,000 rows

This master dataset feeds into:
- Causal analysis (IV, SCM, VAR)
- ML models (LSTM, XGBoost, GNN)
- Scenario simulations
- Vulnerability index

---

## QUESTIONS?

Contact project lead if:
- Files don't match descriptions above
- Data extraction fails (especially I-O PDF)
- Need clarification on calculations
- Encounter missing data / data quality issues

**Target completion:** End of Week 1 (Day 5)