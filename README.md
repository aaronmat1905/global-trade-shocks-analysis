# Global Commodity Shocks, International Trade Linkages, and Economic Resilience: Causal Impacts and Predictive Modelling of Sectoral Stress
## ADA Course Project **(UE23AM343AB1)**

This repository investigates how global commodity shocks—including energy, food, and metal price volatility—propagate through international trade networks and affect sectoral stress and economic resilience. By analyzing trade linkages with major partners such as the U.S., China, the EU, and Gulf economies, the study identifies causal pathways through which external shocks impact agriculture, manufacturing, energy-intensive industries, and exports. Predictive modeling techniques are applied to quantify vulnerabilities and assess resilience under different shock scenarios.

---

## Abstract

Global commodity volatility can create cascading effects in domestic economies, especially through trade networks. This project integrates **high-frequency commodity price data**, **detailed bilateral trade flows**, **causal inference methods**, and **predictive machine learning models** to:  

- Understand how external shocks transmit through trade linkages.  
- Forecast sector-level vulnerabilities using time-series neural networks and gradient boosting.  
- Develop policy-relevant resilience metrics for key economic sectors.  

Unlike prior work, which often focuses on aggregate effects or isolated shocks, this study combines multiple data dimensions to provide a granular, integrated view of shock propagation and sectoral resilience.

---

## Datasets

- **Global commodity prices (energy, food, metals):** [World Bank Pink Sheet](https://www.worldbank.org/en/research/commodity-markets)  
- **Bilateral trade flows:** [UN Comtrade](https://comtrade.un.org/)  
- **Sectoral output and value-added:** [MOSPI](http://mospi.nic.in/)  
- **Exchange rates and macroeconomic controls:** [RBI database](https://www.rbi.org.in/)  
- **Partner-country macro indicators:** [OECD.Stat](https://stats.oecd.org/) and [IMF Direction of Trade Statistics](https://data.imf.org/?sk=9D6028D4-F14A-464C-A2F2-59B2CD424B85)

---

## Methodology

1. **Data Collection and Preprocessing**  
   - Aggregate commodity prices, trade flows, and sectoral output.  
   - Identify major trade partners and sector-specific exposures.

2. **Causal Inference**  
   - Use instrumental variables and synthetic control methods to identify causal transmission channels.  
   - Map the effect of commodity shocks on sectoral performance.

3. **Predictive Modeling**  
   - Apply machine learning methods such as tree-based models and gradient boosting to forecast sectoral stress.  
   - Evaluate model performance using standard metrics (RMSE, MAE, R², MAPE).

4. **Resilience Assessment**  
   - Develop quantitative metrics to assess sectoral resilience under varying shock scenarios.  
   - Analyze which sectors are most vulnerable and where trade linkages amplify or dampen shocks.

---

## Project Results Document (Summary)

A consolidated results document for the "Global Commodity Shocks and Trade Networks" project summarizes all findings, diagnostics, causal estimates, and visualizations. 

**Key High-Level Takeaways:**
- **Team:** StatGeeks (Aaron T. Mathew, Preetham VJ, Akarsh T, Anirudh K) — **Date:** November 2025
- **Core Finding:** Structural distribution shifts (pre-/post-2020 COVID and Ukraine shock) materially affect predictive generalization; causal and network analyses identify critical chokepoints (Petroleum, Trade) and policy-targetable vulnerable sectors.
- **Dataset:** Unified master dataset (3,476 rows × 93 variables), production network (~131 sectors, ~3,401 edges).
- **Sprint 1 (Data & Network):** Constructed complete I-O derived network with technical coefficients, Leontief inverse matrices, and centrality measures.
- **Sprint 2 (Causal Analysis):** IV analysis confirmed energy shocks cause ~4.81% IIP decline (10% price increase); identified network bottlenecks via Betweenness Centrality and shock multiplier effects (>2x systemic amplification).
- **Sprint 3 (Modeling & Policy):** Tree-based models (tuned Random Forest / XGBoost) proved most robust to distribution shifts; Causal ML identified heterogeneous treatment effects across sectors; policy recommendations target Top 5–7 vulnerable sectors for maximum marginal benefit.

For full methodological details, statistical tables, and comprehensive figures, consult the consolidated "Project Results Document" in the deliverables folder or project archive.

---

## Directory Structure

```
global-trade-shocks-analysis/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   ├── raw/                          # Original downloaded data (never modify)
│   │   ├── CMO-Historical-Data-Monthly.xlsx
│   │   ├── IMTSTrade.csv
│   │   ├── WITS-Partner.xlsx
│   │   ├── IndexofIndustrialProduction.xlsx
│   │   ├── WholesalePriceIndexMonthlyData.xlsx
│   │   ├── GDP_Constant.xlsx
│   │   ├── GDP_Current.xlsx
│   │   ├── GVA_Current.xlsx
│   │   └── OECD_file.csv
│   │
│   ├── processed/                    # Cleaned, transformed data
│   │   ├── proc_cmo_monthly.csv                # Commodity prices with shocks
│   │   ├── climate_oni_clean.csv               # Climate indices (ONI)
│   │   ├── trade_india_bilateral.csv           # Bilateral trade flows
│   │   ├── country_mapping.csv                 # ISO3 codes and regions
│   │   ├── iso_dataset_enriched.csv            # Trade data with ISO codes
│   │   ├── iip_sectoral.csv                    # Industrial production indices
│   │   ├── wpi_inflation.csv                   # Wholesale price inflation
│   │   ├── gdp_quarterly.csv                   # GDP with growth rates
│   │   ├── global_macro.csv                    # OECD G20 data
│   │   ├── MOSPI Matrix Final - ALL.csv        # Input-Output matrix
│   │   ├── MOSPI_Cleaned_non_matrix.xlsx       # I-O non-matrix data
│   │   ├── master_dataset.csv                  # Complete merged dataset
│   │   ├── master_dataset_filtered.csv         # Filtered (2010-2024)
│   │   ├── full_ml_dataset.csv                 # ML-ready dataset with engineered features
│   │   └── master_dataset_columns.csv          # Metadata
│   │
│   ├── processed_io_data/            # Network analysis outputs
│   │   ├── technical_coefficients.csv
│   │   ├── leontief_inverse.csv
│   │   ├── production_network_nodes.csv
│   │   ├── production_network_edges.csv
│   │   └── network_metrics.csv
│   │
│   ├── external/                     # Third-party datasets (if any)
│   └── data-dictionary.md            # Data documentation
│
├── networks/                         # Network graph objects
│   ├── trade_network_full.gpickle
│   ├── trade_network_full.graphml
│   ├── trade_network_energy.gpickle
│   ├── trade_network_energy.graphml
│   ├── trade_network_food.gpickle
│   ├── trade_network_food.graphml
│   ├── trade_network_metals.gpickle
│   ├── trade_network_metals.graphml
│   ├── production_network.gpickle
│   ├── production_network.graphml
│   ├── centrality_degree.csv
│   ├── centrality_betweenness.csv
│   ├── centrality_closeness.csv
│   ├── centrality_eigenvector.csv
│   ├── centrality_pagerank.csv
│   ├── centrality_all.csv
│   ├── network_topology_metrics.csv
│   ├── commodity_network_stats.csv
│   └── trade_network.gephi          # Gephi project file
│
├── src/                              # Source code (Python scripts)
│   ├── __init__.py
│   │
│   ├── data_collection/
│   │   ├── __init__.py
│   │   └── download_worldbank.py         # World Bank data fetcher
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── clean_data.py                 # Complete data cleaning pipeline
│   │   ├── create_master_dataset.py      # Master dataset creation
│   │   ├── clean_commodity_prices.py     # Commodity price cleaning
│   │   └── README.md                     # Data processing documentation
│   │
│   ├── network_analysis/
│   │   ├── __init__.py
│   │   ├── process_io_table.py           # I-O table processing & network metrics
│   │   ├── build_trade_network.py        # Trade network construction
│   │   └── visualize_networks.py         # Network visualization utilities
│   │
│   ├── causal_inference/
│   │   ├── __init__.py
│   │   ├── instrumental_variables.py
│   │   ├── synthetic_control.py
│   │   ├── var_granger.py
│   │   └── causal_utils.py
│   │
│   ├── feature_engineering/
│   │   ├── __init__.py
│   │   ├── extract_network_features.py
│   │   ├── create_lag_features.py
│   │   ├── create_volatility_features.py
│   │   ├── create_shock_indicators.py
│   │   ├── create_interaction_features.py
│   │   └── feature_selection.py
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── baseline_models.py
│   │   ├── lstm_model.py
│   │   ├── xgboost_model.py
│   │   ├── gnn_model.py
│   │   ├── ensemble_model.py
│   │   ├── model_evaluation.py
│   │   └── model_utils.py
│   │
│   ├── scenario_analysis/
│   │   ├── __init__.py
│   │   ├── historical_scenarios.py
│   │   ├── counterfactual_scenarios.py
│   │   ├── policy_interventions.py
│   │   └── vulnerability_index.py
│   │
│   ├── visualization/
│   │   ├── __init__.py
│   │   ├── plot_networks.py
│   │   ├── plot_causal_results.py
│   │   ├── plot_model_results.py
│   │   ├── plot_scenarios.py
│   │   └── viz_utils.py
│   │
│   └── dashboard/
│       ├── __init__.py
│       ├── app.py                    # Main Streamlit app
│       ├── pages/
│       │   ├── 1_Home.py
│       │   ├── 2_Networks.py
│       │   ├── 3_Predictions.py
│       │   └── 4_Scenarios.py
│       └── components/
│           ├── __init__.py
│           ├── network_viz.py
│           ├── prediction_viz.py
│           └── scenario_viz.py
│
├── notebooks/                        # Jupyter notebooks for exploration & development
│   ├── README.md                     # Notebook overview and usage guide
│   ├── s1_DataCleaning.ipynb         # Sprint 1: Data cleaning and EDA
│   │   └── Purpose: Exploratory cleaning steps, outlier handling, temporal alignment.
│   │       Outputs: Insights fed into src/data_processing/clean_data.py
│   │
│   ├── s1_IOTableProcessing.ipynb    # Sprint 1: I-O table processing
│   │   └── Purpose: Technical coefficients, Leontief inverse, network metrics (degree, betweenness, PageRank).
│   │       Outputs: Network CSV exports, feed into src/network_analysis/process_io_table.py
│   │
│   ├── s1_CreateMasterDataset.ipynb  # Sprint 1: Master dataset creation & feature engineering
│   │   └── Purpose: Merge all processed data, I-O sector mapping (22 manufacturing sectors),
│   │       derive interaction terms, lagged variables for econometric analysis.
│   │       Outputs: data/processed/master_dataset.csv (3,476 rows × 93 cols)
│   │
│   ├── s2_CausalAnalysis.ipynb       # Sprint 2: Causal inference (IV, Synthetic Control, VAR)
│   │   └── Purpose: Instrumental Variables (2SLS) with ONI & OPEC quotas; 
│   │       Synthetic Control for shock events (2008, 2014, 2022);
│   │       VAR/Granger Causality & Impulse Response Analysis.
│   │       Outputs: Causal estimates, IRF plots, robustness checks
│   │
│   ├── s2_NetworkDynamics.ipynb      # Sprint 2: Network resilience & bottleneck analysis
│   │   └── Purpose: Shock propagation simulations, centrality-vulnerability linkages,
│   │       production network dynamics under targeted sector failures.
│   │       Outputs: Shock multiplier estimates, network robustness metrics
│   │
│   ├── s3_FeatureEngineering.ipynb   # Sprint 3: Advanced feature engineering
│   │   └── Purpose: Create lag features, volatility measures, shock indicators,
│   │       interaction terms; dimensionality reduction (150+ → 50 features).
│   │       Outputs: Feature importance rankings, engineered datasets
│   │
│   ├── s3_TreeBasedModels.ipynb      # Sprint 3: Tree-based predictive models
│   │   └── Purpose: End-to-end ML pipeline: 
│   │       - Target capping (2σ outlier handling)
│   │       - Train/test split diagnostics (temporal coherence)
│   │       - Feature scaling (StandardScaler)
│   │       - Baseline models (Mean, Linear Regression)
│   │       - Random Forest baseline & hyperparameter tuning (RandomizedSearchCV)
│   │       - XGBoost baseline & tuning with early stopping
│   │       - Feature importance analysis (RF vs XGB comparison)
│   │       - Weighted ensemble optimization
│   │       - Comprehensive error analysis (sector-level, temporal, residuals)
│   │       - Distribution shift diagnostics (KS test, train vs test)
│   │       Outputs: Model artifacts (pkl), comparison tables, diagnostic plots
│   │
│   └── s3_CausalML.ipynb             # Sprint 3: Causal Machine Learning (Heterogeneous Effects)
│       └── Purpose: Causal Forests, R-learner, S-learner for heterogeneous treatment effects;
│           vulnerability classification; policy targeting optimization.
│           Outputs: CATE distributions, policy benefit frontier

│
├── models/                           # Saved trained models
│   ├── baseline_ols.pkl
│   ├── baseline_rf.pkl
│   ├── lstm_energy.h5
│   ├── lstm_manufacturing.h5
│   ├── lstm_agriculture.h5
│   ├── lstm_services.h5
│   ├── lstm_exports.h5
│   ├── xgboost_main.pkl
│   ├── xgboost_tuned.pkl
│   ├── gnn_production.pt
│   ├── gnn_trade.pt
│   ├── ensemble_stacked.pkl
│   └── model_metadata.json
│
├── outputs/                          # All output files (models, figures, tables)
│   ├── models/                       # Trained model artifacts
│   │   ├── linear_regression_baseline.pkl
│   │   ├── random_forest_baseline.pkl
│   │   ├── random_forest_tuned.pkl
│   │   ├── xgboost_baseline.pkl
│   │   └── xgboost_tuned.pkl
│   │
│   ├── figures/                      # Publication-quality visualizations
│   │   ├── target_distribution_analysis.png
│   │   │   └── Raw vs 2σ-capped histograms & boxplots
│   │   ├── feature_importance_comparison.png
│   │   │   └── Side-by-side top-30 features: Random Forest vs XGBoost
│   │   ├── model_comparison.png
│   │   │   └── Multi-panel comparison (R², RMSE, MAE, MAPE) across all models
│   │   ├── sector_predictions.png
│   │   │   └── Time-series actual vs predicted for top-5 sectors
│   │   ├── sector_error_analysis.png
│   │   │   └── Top sectors by MAE & error vs sample size
│   │   ├── temporal_error_analysis.png
│   │   │   └── MAE and bias trends over time (year-quarter)
│   │   ├── residual_diagnostics.png
│   │   │   └── Residuals vs predicted, histogram + normal overlay, Q-Q, time series
│   │   ├── distribution_shift_analysis.png
│   │   │   └── Train vs Test overlapping histograms, boxplots, CDFs
│   │   └── (additional sector-specific and network plots as generated)
│   │
│   ├── tables/                       # CSV, LaTeX, and summary tables
│   │   ├── model_comparison.csv
│   │   │   └── RMSE, MAE, R², MAPE for all models
│   │   ├── feature_importance.csv
│   │   │   └── Feature rankings from RF, XGB, and ensemble
│   │   ├── sector_error_analysis.csv
│   │   │   └── MAE, Std, Max Error, Bias per sector
│   │   ├── temporal_error_analysis.csv
│   │   │   └── Error metrics by year-quarter
│   │   ├── distribution_shift_summary.csv
│   │   │   └── Train vs Test statistics (mean, std, min, max, KS test)
│   │   └── (additional causal, network, and scenario tables)
│   │
│   └── data_quality/                 # Data validation reports
│       ├── commodity_prices_validation.txt
│       ├── trade_data_validation.txt
│       ├── master_dataset_summary.txt
│       └── missing_values_report.csv
│
├── sprint_3_output/                  # Sprint 3 experiment-specific outputs
│   ├── target_distribution_analysis.png
│   ├── feature_importance_comparison.png
│   └── (other intermediate or exploratory artifacts)
│
├── sprint3_opts/                     # Alternative tuning experiment outputs
│   ├── models/                       # Model snapshots from different tuning runs
│   └── (other experiment-specific files)
│
├── docs/                             # Documentation
│   ├── data_sources.md
│   ├── data_dictionary.xlsx
│   ├── master_dataset_dictionary.xlsx
│   ├── feature_dictionary.xlsx
│   ├── mospi_io_processing_notes.md
│   ├── methodology_notes.md
│   ├── api_usage_guide.md
│   └── troubleshooting.md
│
├── presentations/                    # Presentation materials
│   ├── sprint1_review.pptx
│   ├── sprint2_review.pptx
│   ├── sprint3_review.pptx
│   ├── final_presentation.pptx
│   └── poster.pdf                    # Optional conference poster
│
├── reports/                          # Written reports
│   ├── drafts/
│   │   ├── sprint1_summary.docx
│   │   ├── sprint2_causal_analysis.docx
│   │   └── sprint3_model_results.docx
│   ├── final_report.pdf
│   ├── final_report.docx
│   ├── executive_summary.pdf
│   └── policy_brief.pdf
│
├── tests/                            # Unit tests (optional but recommended)
│   ├── __init__.py
│   ├── test_data_processing.py
│   ├── test_network_analysis.py
│   ├── test_models.py
│   └── test_utils.py
│
└── logs/                             # Log files
    ├── data_download.log
    ├── model_training.log
    └── error.log

```
---

### 📊 Key Outputs & Artifacts

#### Models (outputs/models/)
- `linear_regression_baseline.pkl`
- `random_forest_baseline.pkl` — Baseline Random Forest
- `random_forest_tuned.pkl` — **Best tree-based model** (R² ≈ 0.017)
- `xgboost_baseline.pkl`
- `xgboost_tuned.pkl` — Tuned XGBoost (R² ≈ 0.011)

#### Figures (outputs/figures/)
**Distribution & Target Analysis:**
- `target_distribution_analysis.png` — Raw vs 2σ-capped histograms & boxplots
- `distribution_shift_analysis.png` — Train vs Test overlap plots, CDF comparison

**Model Performance:**
- `model_comparison.png` — Multi-metric bar charts (R², RMSE, MAE, MAPE)
- `feature_importance_comparison.png` — Top-30 features from RF & XGB side-by-side

**Error Diagnostics:**
- `sector_predictions.png` — Time-series actual vs predicted for top-5 sectors
- `sector_error_analysis.png` — MAE rankings and error vs sample size
- `temporal_error_analysis.png` — MAE & bias trends by year-quarter
- `residual_diagnostics.png` — Residuals vs predicted, histogram, Q-Q, time series

#### Tables (outputs/tables/)
- `model_comparison.csv` — RMSE, MAE, R², MAPE for all models
- `feature_importance.csv` — RF, XGB, and average importance rankings
- `sector_error_analysis.csv` — Per-sector MAE, std, bias, sample size
- `temporal_error_analysis.csv` — Per-quarter MAE, bias, sample size
- `distribution_shift_summary.csv` — Train/test statistics & KS test results

#### Alternative Outputs
- `sprint_3_output/` — Experiment-specific artifacts (e.g., target distribution plots)
- `sprint3_opts/models/` — Alternative tuning run snapshots

---

## Quick Start

### 1. Regenerate Processed Data
To rebuild all cleaned and processed datasets from raw files:

```bash
# Install dependencies
pip install -r requirements.txt

# Run the full cleaning pipeline
python src/data_processing/clean_data.py

# Process I-O tables and calculate network metrics
python src/network_analysis/process_io_table.py

# Create master dataset and export
python src/data_processing/create_master_dataset.py
```

All outputs saved to `data/processed/` and `data/processed_io_data/`.

### 2. Run Notebook Workflows
Each notebook is self-contained and documents its purpose in the header:

```bash
jupyter notebook notebooks/s3_TreeBasedModels.ipynb
# (or any other notebook)
```

Notebooks import data from `data/processed/` and write outputs to `outputs/` and/or `sprint_3_output/`.

### 3. Access Key Results
- **Model comparison:** `outputs/tables/model_comparison.csv`
- **Feature importance:** `outputs/tables/feature_importance.csv`
- **Model artifacts:** `outputs/models/*.pkl`
- **Visualizations:** `outputs/figures/`

---

## Key Findings Summary

### Distribution Shift (Critical for Modeling)
The project identified a **significant structural break** between training (pre-2020: volatile, COVID-affected) and test (post-2020: recovery) periods, confirmed by Kolmogorov-Smirnov test. This explains why:
- **Linear models failed** (R² ≈ −36)
- **Tree-based models were more robust** (tuned RF: R² ≈ 0.017)
- **Deep learning (LSTM) overfitted** — learned high-volatility patterns that don't apply to stable test period

### Causal Impact Estimates
- **Energy shocks:** 10% oil price increase → −4.81% IIP (all manufacturing: −8.0%), p < 0.05
- **Food shocks:** wheat prices showed negative coefficient (−2.55) but not statistically significant (p > 0.05)
- **Instruments validated:** Sargan-Hansen test p-values > 0.05 (exogeneity confirmed)

### Network Vulnerabilities
- **Critical bottlenecks:** Petroleum Products, Trade, Electricity (ranked by Betweenness Centrality)
- **Shock multiplier:** 10% output shock → 2.19x cumulative impact via Leontief propagation
- **Scale-free topology:** Robust to random failures, vulnerable to targeted attacks on top ~15% central nodes

### Policy Recommendations
- **Targeting strategy:** Policy Benefit Frontier is concave → diminishing returns beyond Top 5–7 sectors
- **Expected benefit:** Mitigation strategy could preserve **0.46% of aggregate IIP growth** during shock
- **High-vulnerability sectors:** Other Manufacturing, Tobacco, Electrical Equipment
- **Most resilient sectors:** Motor Vehicles, Pharmaceuticals, Basic Metals

---

## Team

1. **Aaron Thomas Mathew** — [GitHub](https://github.com/aaronmat1905)
2. **Preetham VJ** — [GitHub](https://github.com/PreethamVJ)
3. **Akarsh T** — [GitHub](https://github.com/Akarsh8T)
4. **Anirudh Krishnan** — [GitHub](https://github.com/Anirudh553)

---

## References

1. Global Supply Chain Reallocation and Shift under Triple Crises: A U.S.-China Perspective  
   [https://arxiv.org/pdf/2508.06828](https://arxiv.org/pdf/2508.06828)  

2. Financial Markets, Financial Institutions, and International Trade: Examining the Causal Links for Indian Economy  
   [https://arxiv.org/pdf/2112.01749](https://arxiv.org/pdf/2112.01749)  

3. The Causal Effects of Commodity Shocks  
   [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5219522](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5219522)

4. Leontief Model & Input-Output Analysis for Supply Chain Shock Propagation  
   [https://mitpress.mit.edu/](https://mitpress.mit.edu/)

---

## License

This project is provided for educational purposes as part of the ADA course project (UE23AM343AB1). 

---

**Last Updated:** November 2025
