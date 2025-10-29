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
   - Apply machine learning methods such as time-series neural networks and gradient boosting to forecast sectoral stress.  
   - Evaluate model performance using standard metrics (RMSE, MAE, etc.).

4. **Resilience Assessment**  
   - Develop quantitative metrics to assess sectoral resilience under varying shock scenarios.  
   - Analyze which sectors are most vulnerable and where trade linkages amplify or dampen shocks.

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
│   │   ├── clean_commodity_prices.py     # Existing placeholder
│   │   └── README.md                     # Data processing documentation
│   │
│   ├── network_analysis/
│   │   ├── __init__.py
│   │   ├── process_io_table.py           # I-O table processing & network metrics
│   │   ├── build_trade_network.py        # Existing placeholder
│   │   └── visualize_networks.py         # Existing placeholder
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
├── notebooks/                        # Jupyter notebooks for exploration
│   ├── data_cleaning.ipynb           # Data cleaning exploration (→ clean_data.py)
│   ├── iotable_processing.ipynb      # I-O table processing (→ process_io_table.py)
│   ├── create_master_dataset.ipynb   # Master dataset creation
│   └── (additional notebooks TBD)
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
├── outputs/                          # All output files
│   ├── figures/                      # Publication-quality visualizations
│   │   ├── networks/
│   │   │   ├── trade_network_gephi_viz.png
│   │   │   ├── production_network_hierarchical.png
│   │   │   ├── network_viz_production.png
│   │   │   ├── network_viz_trade.png
│   │   │   ├── io_matrix_heatmap.png
│   │   │   └── interactive_trade_network.html
│   │   ├── causal/
│   │   │   ├── iv_results.png
│   │   │   ├── iv_first_stage.png
│   │   │   ├── scm_event_2008_results.png
│   │   │   ├── scm_event_2014_results.png
│   │   │   ├── scm_event_2022_results.png
│   │   │   ├── scm_placebo_test.png
│   │   │   ├── var_irf_grid.png
│   │   │   └── var_stability_roots.png
│   │   ├── models/
│   │   │   ├── baseline_predictions.png
│   │   │   ├── lstm_learning_curves.png
│   │   │   ├── xgboost_feature_importance.png
│   │   │   ├── gnn_attention_weights.png
│   │   │   ├── model_comparison_rmse.png
│   │   │   ├── prediction_vs_actual_sector1.png
│   │   │   ├── prediction_vs_actual_sector2.png
│   │   │   ├── prediction_vs_actual_sector3.png
│   │   │   ├── prediction_vs_actual_sector4.png
│   │   │   ├── prediction_vs_actual_sector5.png
│   │   │   └── residual_plots.png
│   │   ├── scenarios/
│   │   │   ├── scenario_2008_impacts.png
│   │   │   ├── scenario_2014_impacts.png
│   │   │   ├── scenario_2022_impacts.png
│   │   │   ├── counterfactual_diversification.png
│   │   │   ├── policy_strategic_reserve.png
│   │   │   ├── policy_hedging.png
│   │   │   ├── vulnerability_heatmap.png
│   │   │   └── scenario_comparison_multi.png
│   │   └── exploratory/
│   │       ├── commodity_price_trends.png
│   │       ├── sectoral_output_trends.png
│   │       ├── feature_correlation_heatmap.png
│   │       └── trade_flow_time_series.png
│   │
│   ├── tables/                       # Formatted tables (CSV, LaTeX, Excel)
│   │   ├── network_metrics/
│   │   │   ├── centrality_summary.csv
│   │   │   ├── centrality_summary.tex
│   │   │   ├── sector_linkages_summary.csv
│   │   │   └── network_topology_summary.csv
│   │   ├── causal/
│   │   │   ├── iv_first_stage.csv
│   │   │   ├── iv_second_stage.csv
│   │   │   ├── iv_robustness.csv
│   │   │   ├── scm_weights_event2008.csv
│   │   │   ├── scm_weights_event2014.csv
│   │   │   ├── scm_weights_event2022.csv
│   │   │   ├── scm_treatment_effects.csv
│   │   │   ├── granger_causality_matrix.csv
│   │   │   ├── var_coefficients.csv
│   │   │   ├── irf_results.csv
│   │   │   └── fevd_results.csv
│   │   ├── models/
│   │   │   ├── baseline_performance.csv
│   │   │   ├── model_comparison.csv
│   │   │   ├── feature_importance.csv
│   │   │   ├── cv_results.csv
│   │   │   └── model_metrics_detailed.csv
│   │   └── scenarios/
│   │       ├── vulnerability_ranking.csv
│   │       ├── scenario_impacts_2008.csv
│   │       ├── scenario_impacts_2014.csv
│   │       ├── scenario_impacts_2022.csv
│   │       ├── counterfactual_results.csv
│   │       └── policy_comparison.csv
│   │
│   └── data_quality/                 # Data validation reports
│       ├── commodity_prices_validation.txt
│       ├── trade_data_validation.txt
│       ├── master_dataset_summary.txt
│       └── missing_values_report.csv
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

## Current Implementation Status

### ✓ Completed Components

#### Data Processing Pipeline
- **[src/data_processing/clean_data.py](src/data_processing/clean_data.py)** - Complete data cleaning pipeline
  - Commodity prices processing (CMO data with shocks, volatility)
  - Climate data (ONI indices with ENSO classification)
  - Trade data processing (bilateral flows by commodity group)
  - IIP sectoral data (industrial production indices)
  - WPI data (wholesale price inflation)
  - GDP data (quarterly estimates with growth rates)
  - OECD data (G20 macro indicators)

- **[src/network_analysis/process_io_table.py](src/network_analysis/process_io_table.py)** - I-O table processing & network analysis
  - Technical coefficients calculation
  - Leontief inverse matrix computation
  - Backward/forward linkage analysis
  - Network centrality metrics (PageRank, betweenness, degree, closeness, eigenvector)
  - Production network edge list generation

- **[src/data_processing/create_master_dataset.py](src/data_processing/create_master_dataset.py)** - Master dataset creation
  - Merges all processed datasets
  - IIP to I-O sector mapping (22 manufacturing sectors)
  - Derived variables & feature engineering
  - Lagged variables for econometric analysis
  - Energy intensity flags & interaction terms

#### Processed Datasets Available
- `data/processed/master_dataset.csv` - **3,476 rows × 93 columns** (2012-2024, 22 sectors)
- All intermediate processed files in `data/processed/`
- Network metrics in `data/processed_io_data/`

#### Documentation
- Complete data processing documentation in [src/data_processing/README.md](src/data_processing/README.md)
- Data dictionary in [data/data-dictionary.md](data/data-dictionary.md)

### 🚧 In Development
- Causal inference methods (IV, Synthetic Control, VAR)
- ML models (LSTM, XGBoost, GNN)
- Scenario analysis & vulnerability assessment
- Interactive dashboard

### 📊 Quick Start

To regenerate all processed data:

```bash
# 1. Clean raw data sources
python src/data_processing/clean_data.py

# 2. Process I-O tables and calculate network metrics
python src/network_analysis/process_io_table.py

# 3. Create master dataset
python src/data_processing/create_master_dataset.py
```

All outputs will be saved to `data/processed/` and `data/processed_io_data/`.

---

## References

1. Global Supply Chain Reallocation and Shift under Triple Crises: A U.S.-China Perspective  
   [https://arxiv.org/pdf/2508.06828](https://arxiv.org/pdf/2508.06828)  

2. Financial Markets, Financial Institutions, and International Trade: Examining the Causal Links for Indian Economy  
   [https://arxiv.org/pdf/2112.01749](https://arxiv.org/pdf/2112.01749)  

3. The Causal Effects of Commodity Shocks  
   [https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5219522](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5219522)  

---

## Team

1. **Aaron Thomas Mathew**: [https://github.com/aaronmat1905](https://github.com/aaronmat1905)
2. **Akarsh T**: [https://github.com/Akarsh8T](https://github.com/Akarsh8T)
3. **Anirudh Krishnan**: [https://github.com/Anirudh553](https://github.com/Anirudh553)
4. **Preetham VJ**: [https://github.com/PreethamVJ](https://github.com/PreethamVJ)
