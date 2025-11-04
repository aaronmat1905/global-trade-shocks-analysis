# 📓 **SPRINT 2: ESSENTIAL NOTEBOOKS (STREAMLINED)**

---

## **🎯 TOTAL: 5 NOTEBOOKS** (Reduced from 7)

---

## **NOTEBOOK 1: Causal Inference (IV + SCM + VAR)**
### `01_causal_analysis.ipynb`

**Days 1-3 | ~40% of Sprint 2**

### **Contents:**

#### **Part A: Instrumental Variables (IV)**
- Load master dataset
- Literature review summary (markdown cells)
- Prepare instruments (OPEC quotas, ONI index)
- **First-stage regressions** (instruments → commodity prices)
- Check F-statistics (>10 threshold)
- **Second-stage 2SLS** (instrumented prices → sectoral IIP)
- **Validity tests:** Sargan-Hansen J-test, Hausman test
- **Robustness:** Pre/post 2015 subsamples, alternative instruments
- Generate IV results tables

#### **Part B: Synthetic Control Method (SCM)**
- Define treatment events (2008 crisis, 2014 oil crash, 2022 Ukraine war)
- Select donor pool (Brazil, Indonesia, Turkey, Mexico, South Africa)
- Construct synthetic India (optimize weights)
- Estimate treatment effects
- **Placebo tests** (run SCM on all donors)
- Create SCM visualizations

#### **Part C: VAR & Granger Causality**
- **Stationarity tests** (ADF tests on all time series)
- Determine optimal lag length (AIC/BIC)
- **Granger causality tests** (commodity prices → sectoral IIP)
- Estimate VAR models (oil, IIP, exchange rate)
- **Impulse Response Functions (IRF)** - shock propagation over 12 months
- **Forecast Error Variance Decomposition (FEVD)** - % variance explained

#### **Deliverables from Notebook 1:**
- `first_stage_results.xlsx`
- `second_stage_results.xlsx`
- `instrument_validity_tests.xlsx`
- `synthetic_india_results.xlsx`
- `granger_causality_matrix.xlsx`
- `var_irf_fevd_results.xlsx`
- Figures: First-stage plots, SCM plots, IRF plots (15-20 figures)

---

## **NOTEBOOK 2: Feature Engineering**
### `02_feature_engineering.ipynb`

**Days 3-4 | ~25% of Sprint 2**

### **Contents:**

#### **Part A: Load Base Data**
- Load master dataset
- Verify data quality
- Check date ranges (2010-2024)

#### **Part B: Create Network Features**
- Already have 7 network metrics from I-O table
- Verify: degree_centrality, betweenness, closeness, eigenvector, pagerank, backward_linkage, forward_linkage

#### **Part C: Create Price Features**
- **Lagged prices:** t-1, t-3, t-6, t-12 for oil, wheat, copper, aluminum, rice (20 features)
- **Volatility:** Rolling std dev (3m, 6m, 12m) for all commodities (15 features)
- **Returns:** Log returns for all prices (5 features)

#### **Part D: Create Shock Indicators**
- Binary shocks: price change > 2σ for all commodities (5 features)
- Positive/negative shocks separately (10 features)
- Duration variables: months since last shock (5 features)

#### **Part E: Create Exposure Features**
- **Energy input share:** From I-O technical coefficients
- **Food input share:** Agricultural + food processing inputs
- **Metal input share:** Iron & steel + non-ferrous inputs
- **Interaction terms:** energy_share × oil_price, food_share × wheat_price (8 features)

#### **Part F: Create Trade Features**
- **HHI (Herfindahl Index):** Import concentration by sector
- **Partner diversification:** Number of import partners
- **Import dependence:** Imports / Total supply
- **Export orientation:** Exports / Output (4 features)

#### **Part G: Create Interaction Features**
- Network × Commodity exposure: degree_centrality × energy_share, etc. (21 features)
- Network × Shocks: betweenness × oil_shock_binary, etc. (14 features)

#### **Part H: Create Temporal Features**
- Cyclical encoding: month_sin, month_cos, quarter_sin, quarter_cos (4 features)
- Time trend (1 feature)
- Month/quarter dummies (14 features)

#### **Part I: Merge All Features**
- Combine all feature categories
- Check for missing values
- Final dataset: **150+ features**

#### **Deliverables from Notebook 2:**
- `ml_dataset_full.csv` (3,600 rows × 150+ columns)
- `feature_dictionary.xlsx` (description of each feature)
- Summary statistics table

---

## **NOTEBOOK 3: Dimensionality Reduction & Feature Selection**
### `03_feature_selection.ipynb`

**Day 5 | ~15% of Sprint 2**

### **Contents:**

#### **Part A: Correlation Analysis**
- Calculate 150×150 correlation matrix
- Identify highly correlated pairs (|r| > 0.9)
- Create correlation heatmap (top 50 features)
- Drop redundant features
- Output: ~130 features

#### **Part B: Variance Inflation Factor (VIF)**
- Calculate VIF for all features
- Iteratively drop features with VIF > 10
- Output: ~110 features

#### **Part C: Random Forest Feature Importance**
- Train baseline Random Forest (quick, 100 trees)
- Extract feature importance (Gini + Permutation)
- Rank all features
- Visualize top 50 features

#### **Part D: Feature Selection Strategy**
- **Strategy 1:** Keep top 50-60 features from Random Forest
- **Strategy 2:** Force-include theory-driven features (network metrics, key prices)
- Final feature set: **55-60 features**

#### **Part E: PCA Analysis (Optional)**
- Apply PCA to network features block (if using)
- Determine components explaining 95% variance
- Decision: Use PCA or keep original features

#### **Part F: Feature Normalization**
- Standardization (Z-score) for continuous variables
- Keep binary variables unchanged
- **Critical:** Calculate μ and σ on training set ONLY

#### **Part G: Train-Test Split**
- **Temporal split:** Train (2010-2020), Test (2021-2024)
- Create validation set (optional): 2019-2020
- Verify no data leakage

#### **Deliverables from Notebook 3:**
- `correlation_matrix.csv`
- `vif_analysis.xlsx`
- `rf_feature_importance.xlsx`
- `final_feature_list.xlsx` (55 selected features)
- `train_set.csv`, `test_set.csv`, `validation_set.csv`
- Figures: Correlation heatmap, feature importance plot (3-5 figures)

---

## **NOTEBOOK 4: ML Modeling & Evaluation**
### `04_ml_models.ipynb`

**Day 6 | ~15% of Sprint 2**

### **Contents:**

#### **Part A: Load Prepared Data**
- Load train/test sets from Notebook 3
- Verify data shapes and distributions

#### **Part B: Baseline Models**
- **OLS Regression:** Simple linear regression
- **LASSO:** With cross-validation for alpha tuning
- **Ridge:** With cross-validation
- Evaluate: R², RMSE, MAE, direction accuracy

#### **Part C: Tree-Based Models**
- **Random Forest:** GridSearchCV (n_estimators, max_depth, min_samples_split)
- **XGBoost:** GridSearchCV (learning_rate, n_estimators, max_depth)
- **LightGBM:** (Optional, if time permits)
- Extract feature importance from best model

#### **Part D: Model Comparison**
- Create comparison table (all models)
- Metrics: R², RMSE, MAE, MAPE, direction accuracy
- Identify best model (likely XGBoost)

#### **Part E: Sector-Specific Analysis**
- Evaluate model performance by sector type:
  - Energy-intensive (Chemicals, Petroleum, Metals)
  - Food-dependent (Food products, Beverages)
  - Export-oriented (Motor vehicles, Electronics)
- Create sector performance table

#### **Part F: Error Analysis**
- Residual plots (predicted vs actual, residuals vs fitted)
- Residuals over time (check autocorrelation)
- Identify worst-predicted periods/sectors

#### **Part G: Feature Importance Interpretation**
- Top 20 features from best model
- Compare with theory/expectations
- Sector-specific feature importance

#### **Deliverables from Notebook 4:**
- `model_comparison_results.xlsx`
- `sector_performance.xlsx`
- `xgboost_feature_importance.xlsx`
- Trained model files: `best_model.pkl`
- Figures: Actual vs predicted, residuals, feature importance (8-10 figures)

---

## **NOTEBOOK 5: Results & Visualization**
### `05_results_documentation.ipynb`

**Day 7 | ~5% of Sprint 2**

### **Contents:**

#### **Part A: Load All Results**
- Import results from Notebooks 1-4
- IV results, SCM results, VAR results, ML results

#### **Part B: Create Publication-Quality Tables**
- **Table 1:** First-stage IV results (F-stats, coefficients)
- **Table 2:** Second-stage 2SLS results (by sector)
- **Table 3:** Instrument validity tests (Sargan-Hansen, Hausman)
- **Table 4:** Synthetic control treatment effects
- **Table 5:** Granger causality matrix
- **Table 6:** ML model comparison
- **Table 7:** Sector vulnerability rankings
- Export to Excel/LaTeX format

#### **Part C: Create All Visualizations**
- **IV plots:** First-stage scatter, coefficient plots with CI
- **SCM plots:** Actual vs synthetic, placebo distribution
- **VAR plots:** Impulse response functions (6-9 IRFs), FEVD bar charts
- **ML plots:** Feature importance, actual vs predicted time series, sector heatmap
- **Network plots:** Production network graph (top 30 sectors)

#### **Part D: Summary Statistics**
- Descriptive stats for all key variables
- By sector type, by time period
- Data quality summary

#### **Part E: Executive Summary Generation**
- Key findings from each method
- Numerical results highlights
- Policy implications bullet points

#### **Deliverables from Notebook 5:**
- `all_tables/` folder (7-10 Excel/CSV files)
- `all_figures/` folder (25-30 PNG files, high-res)
- `executive_summary.md`
- `sprint2_results_report.pdf` (automated from notebook)

---

## **📊 WORKFLOW DIAGRAM**

```
START
  ↓
[Notebook 0: Setup] ← Run once, defines all paths/functions
  ↓
[Notebook 1: Causal Analysis] ← Days 1-3
  ├─ IV Analysis
  ├─ Synthetic Control
  └─ VAR/Granger
  ↓
  Outputs: Causal evidence results
  ↓
[Notebook 2: Feature Engineering] ← Days 3-4
  ├─ Create 150+ features
  └─ Merge into ml_dataset_full.csv
  ↓
[Notebook 3: Feature Selection] ← Day 5
  ├─ Correlation analysis
  ├─ VIF reduction
  ├─ RF feature importance
  └─ Create train/test split
  ↓
  Outputs: train_set.csv, test_set.csv (55 features)
  ↓
[Notebook 4: ML Modeling] ← Day 6
  ├─ Train 5-6 models
  ├─ Model comparison
  └─ Sector-specific evaluation
  ↓
  Outputs: model_comparison_results.xlsx, best_model.pkl
  ↓
[Notebook 5: Results & Visualization] ← Day 7
  ├─ Compile all tables
  ├─ Generate all figures
  └─ Write executive summary
  ↓
END → Sprint 2 Deliverables Complete
```

---

## **⏱️ TIME ALLOCATION**

| Notebook | Days | Hours | % of Sprint |
|----------|------|-------|-------------|
| 1. Causal Analysis | 1-3 | 24h | 40% |
| 2. Feature Engineering | 3-4 | 16h | 25% |
| 3. Feature Selection | 5 | 8h | 15% |
| 4. ML Modeling | 6 | 8h | 15% |
| 5. Results/Viz | 7 | 4h | 5% |
| **TOTAL** | **7 days** | **60h** | **100%** |

---

## **✅ DEPENDENCIES BETWEEN NOTEBOOKS**

- **Notebook 1 (Causal):** Independent, can start immediately
- **Notebook 2 (Features):** Independent, can run parallel to Notebook 1
- **Notebook 3 (Selection):** Requires Notebook 2 output (`ml_dataset_full.csv`)
- **Notebook 4 (ML Models):** Requires Notebook 3 output (`train_set.csv`, `test_set.csv`)
- **Notebook 5 (Results):** Requires ALL previous notebooks' outputs

**Parallelization Strategy:**
- Days 1-2: Run Notebook 1 (Team Member A)
- Days 1-2: Run Notebook 2 (Team Member B) ← Can work simultaneously
- Day 3: Both work on Notebook 3
- Day 6: Both work on Notebook 4
- Day 7: Collaborate on Notebook 5

---

## **🎯 KEY SUCCESS METRICS PER NOTEBOOK**

### **Notebook 1 Success:**
✅ F-statistics > 10 for all first-stage regressions  
✅ Sargan-Hansen p-value > 0.05  
✅ 2SLS coefficients economically interpretable  
✅ SCM pre-treatment fit R² > 0.90  
✅ IRFs show expected patterns (negative response to price shocks)

### **Notebook 2 Success:**
✅ 150+ features created  
✅ No missing values in final dataset  
✅ Feature dictionary complete (all features documented)

### **Notebook 3 Success:**
✅ All VIF < 10  
✅ Final feature set: 50-60 features  
✅ Train/test split with no data leakage  
✅ Feature importance plot generated

### **Notebook 4 Success:**
✅ XGBoost R² > 0.55 on test set  
✅ 5+ models trained and compared  
✅ Sector-specific analysis complete  
✅ Best model saved and reproducible

### **Notebook 5 Success:**
✅ All tables formatted and publication-ready  
✅ 25-30 high-quality figures generated  
✅ Executive summary written  
✅ All results can be reproduced from notebooks

---

## **🚨 CRITICAL REMINDERS**

1. **Run notebooks in order** (1 → 2 → 3 → 4 → 5)
2. **Save intermediate outputs** after each notebook
3. **Document assumptions** in markdown cells
4. **Use version control** (Git) - commit after each notebook completion
5. **Set random seeds** for reproducibility (`random_state=42`)

---

**This streamlined 5-notebook structure eliminates redundancy while covering all Sprint 2 requirements. You'll have clear outputs from each notebook that feed into the next, culminating in publication-ready results.** 🚀