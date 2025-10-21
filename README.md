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

Global_Commodity_Shocks_Trade_Networks/
│
├── README.md
├── requirements.txt
├── setup.bat                          # Windows batch file for auto-setup
├── setup.sh                           # Linux/Mac shell script for auto-setup
├── .gitignore
│
├── data/
│   ├── raw/                          # Original downloaded data (never modify)
│   │   ├── commodity_prices/
│   │   │   └── wb_pink_sheet_commodities.xlsx
│   │   ├── trade/
│   │   │   ├── comtrade_india_bilateral_raw.csv
│   │   │   └── comtrade_responses/   # API JSON responses
│   │   ├── input_output/
│   │   │   ├── mospi_io_2015_16_use.csv
│   │   │   ├── mospi_io_2015_16_make.csv
│   │   │   └── mospi_io_2020_21_supply_use.xlsx
│   │   ├── macroeconomic/
│   │   │   ├── rbi_iip.csv
│   │   │   ├── rbi_wpi.csv
│   │   │   ├── rbi_gdp.csv
│   │   │   ├── rbi_exchange_rate.csv
│   │   │   └── rbi_trade.csv
│   │   ├── global/
│   │   │   ├── oecd_gdp_growth.csv
│   │   │   ├── oecd_commodity_indices.csv
│   │   │   ├── oecd_trade_volumes.csv
│   │   │   └── imf_ifs_data.csv
│   │   └── instruments/
│   │       ├── opec_production.csv
│   │       ├── opec_quota_decisions.csv
│   │       ├── noaa_enso_indices.csv
│   │       └── spei_drought_indices.csv
│   │
│   ├── processed/                    # Cleaned, transformed data
│   │   ├── commodity_prices_clean.csv
│   │   ├── trade_flows_clean.csv
│   │   ├── trade_energy_clean.csv
│   │   ├── trade_food_clean.csv
│   │   ├── trade_metals_clean.csv
│   │   ├── rbi_sectoral_clean.csv
│   │   ├── io_coefficient_matrix.csv
│   │   ├── io_make_matrix.csv
│   │   ├── leontief_inverse.csv
│   │   ├── sector_classification.csv
│   │   ├── sector_linkages.csv
│   │   ├── network_features.csv
│   │   ├── trade_exposure.csv
│   │   ├── instruments.csv
│   │   ├── iv_regression_data.csv
│   │   ├── scm_donor_pool.csv
│   │   ├── scm_predictors.csv
│   │   ├── features_engineered.csv
│   │   ├── features_normalized.csv
│   │   ├── master_dataset.csv
│   │   ├── train.csv
│   │   └── test.csv
│   │
│   └── external/                     # Third-party datasets (if any)
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
│   │   ├── download_worldbank.py
│   │   ├── download_comtrade.py
│   │   ├── download_mospi.py
│   │   ├── download_rbi.py
│   │   ├── download_oecd.py
│   │   └── download_instruments.py
│   │
│   ├── data_processing/
│   │   ├── __init__.py
│   │   ├── clean_commodity_prices.py
│   │   ├── clean_trade_data.py
│   │   ├── clean_macro_data.py
│   │   ├── process_io_tables.py
│   │   ├── merge_master_dataset.py
│   │   └── utils.py
│   │
│   ├── network_analysis/
│   │   ├── __init__.py
│   │   ├── build_trade_network.py
│   │   ├── build_production_network.py
│   │   ├── calculate_centrality.py
│   │   ├── calculate_linkages.py
│   │   ├── network_topology.py
│   │   └── visualize_networks.py
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
│   ├── 01_data_exploration.ipynb
│   ├── 02_network_construction.ipynb
│   ├── 03_causal_analysis.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_model_training.ipynb
│   ├── 06_scenario_simulation.ipynb
│   └── Tutorial_Reproducing_Results.ipynb
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
