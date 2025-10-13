# Global Commodity Shocks, International Trade Linkages, and Economic Resilience: Causal Impacts and Predictive Modelling of Sectoral Stress

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

global-commodity-shocks/
│
├── data/                  # Raw and processed datasets
├── models/                # ML models and causal inference scripts
├── experiments/           # Configurations, evaluation scripts, results
├── notebooks/             # Exploratory data analysis and modeling workflows
├── utils/                 # Helper functions and preprocessing tools
└── README.md

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

**Aaron Thomas Mathew**: [https://github.com/aaronmat1905](https://github.com/aaronmat1905)
**Akarsh T**: [https://github.com/placeholder](https://github.com/placeholder)
**Anirudh Krishnan**: [https://github.com/placeholder](https://github.com/placeholder)
**Preetham VJ**: [https://github.com/PreethamVJ](https://github.com/PreethamVJ)
