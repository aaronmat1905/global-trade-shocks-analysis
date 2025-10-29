# Technical Roadmap: Commodity Shocks Project

## Phase 1: Data Preparation & Setup
- **Load & merge datasets**: commodity prices, OPEC quotas, sectoral IIP (139 sectors), trade data
- **Time-series alignment**: ensure all data on same date index (monthly/quarterly)
- **Handle missing values & outliers**: interpolation, winsorization
- **Output**: Clean master dataset ready for analysis

---

## Sprint 2: Causal Evidence (Prove "Why")

### Epic 2.1: Instrumental Variables (2SLS)
**Goal**: Prove commodity prices *cause* sectoral output changes (not the reverse)

*Code steps:*
1. **First-stage regression**: OPEC quotas/weather → oil prices
   - Calculate F-statistic (must be > 10)
2. **Second-stage regression (2SLS)**: Instrumented prices → sectoral output
   - Run for each of 139 sectors
3. **Validity tests**: Sargan-Hansen J-test (check p-value > 0.05)
4. **Robustness**: Re-run on pre/post-2015 subsamples
5. **Output**: Table of coefficients + significance

**Tools**: `statsmodels` (OLS/2SLS), `linearmodels` (IV2SLS)

---

### Epic 2.2: Synthetic Control Method (SCM)
**Goal**: Estimate counterfactual—what would India look like without 2008/2014/2022 shocks?

*Code steps:*
1. **Define events**: 2008-09, 2014-06, 2022-02 as treatment dates
2. **Select donor pool**: Brazil, Indonesia, Turkey, Mexico, South Africa
3. **Collect predictors**: GDP per capita, trade openness, commodity dependence (pre-treatment)
4. **Optimize weights**: minimize difference between real India vs. donor average (pre-treatment)
5. **Estimate effect**: actual India - synthetic India (post-treatment)
6. **Placebo tests**: run same analysis on all donor countries (should show no effect)
7. **Output**: Graphs of actual vs. synthetic trajectories + treatment effect magnitude

**Tools**: `synth_id`, `cvxpy` (optimization)

---

### Epic 2.3: VAR & Granger Causality
**Goal**: Test temporal causation + measure dynamic responses

*Code steps:*
1. **Stationarity test**: ADF test on all time series (reject H0 = non-stationary)
2. **Differencing**: If non-stationary, take first differences
3. **Optimal lags**: Use AIC/BIC criteria (typically 1-4 months)
4. **Granger causality**: Do lagged prices help predict sectoral output? (F-test)
5. **VAR model**: Estimate system of equations (oil price, exchange rate, sectoral IIP)
6. **Impulse responses**: Shock oil price +1 SD, trace effect on sectors over 12 months
7. **Variance decomposition**: "50% of sector X volatility comes from oil shocks"
8. **Stability check**: All eigenvalues inside unit circle
9. **Output**: IRF plots with 95% confidence bands + FEVD table

**Tools**: `statsmodels.tsa.VAR`, `matplotlib` (plotting)

---

### Epic 2.4-2.5: Feature Engineering & Selection
**Goal**: Create 150+ predictive features, reduce to 50 best ones

*Code steps:*

**Feature Engineering (Epic 2.4):**
1. Network centrality: degree, betweenness, closeness for all 139 sectors
2. Lagged prices: 1, 3, 6, 12-month lags of commodity prices
3. Volatility: rolling 3, 6, 12-month standard deviations
4. Shock indicators: binary (price change > 2 std dev?)
5. Exposure: energy input share, food input share (from input-output tables)
6. Trade: HHI index, partner diversification
7. Interactions: centrality × commodity exposure
8. Temporal: month, quarter, year, cyclical encodings (sin/cos)
9. **Output**: master dataset with 150+ columns

**Feature Selection (Epic 2.5):**
1. Correlation matrix: drop features with |r| > 0.9 (multicollinearity)
2. VIF: drop features with VIF > 10
3. Random Forest importance: rank all features, keep top 50
4. PCA (if needed): retain 95% variance explained
5. Normalization: standardize to mean=0, std=1
6. Train-test split: 80% (2010-2020) / 20% (2021-2024)
7. **Output**: Clean dataset, 50 features, train/test indices

**Tools**: `pandas`, `scikit-learn` (preprocessing, feature_selection), `networkx` (centrality)

---

## Sprint 3: Predictive Modeling

### Epic 3.1: Baseline & LSTM
**Goal**: Train neural networks to predict sectoral stress

*Code steps:*
1. **Baseline models**: Moving average, linear regression (for comparison)
2. **LSTM architecture**: 2-3 LSTM layers → dropout → dense output layer
3. **Sequence creation**: Convert time series into rolling 12-month windows
4. **Training**: Adam optimizer, MSE loss, early stopping on validation set
5. **Hyperparameter tuning**: grid search over [units, dropout, learning_rate]
6. **Sector-specific LSTMs**: Train separate models for 5 key sectors
7. **Evaluation**: Calculate RMSE, MAE, MAPE on test set
8. **Output**: Learning curves, test set predictions

**Tools**: `TensorFlow/Keras`, `scikit-learn` (metrics)

---

### Epic 3.2: XGBoost & Ensemble
**Goal**: Gradient boosting + model stacking

*Code steps:*
1. **XGBoost**: Train on all 50 features with cross-validation
2. **Hyperparameter tuning**: grid search over [max_depth, learning_rate, n_estimators]
3. **Feature importance**: Extract top 30 predictive features
4. **Random Forest**: Alternative baseline
5. **Ensemble stacking**: Meta-learner combines LSTM + XGBoost predictions
6. **Time-series CV**: Expanding window (don't use future data for past predictions)
7. **Output**: Model comparison table (all models × all metrics)

**Tools**: `xgboost`, `sklearn.ensemble`, `scikit-learn` (cross_val_score)

---

### Epic 3.3: Graph Neural Networks
**Goal**: Exploit production network structure

*Code steps:*
1. **Setup PyTorch Geometric**: install `torch_geometric`
2. **Graph format**: Convert input-output table → node features + edge indices
   - Nodes = 139 sectors
   - Edges = supplier-buyer relationships
   - Features = commodity exposure, trade data
3. **GNN architecture**: 2-3 GraphSAGE layers + global pooling + output
4. **Training**: Predict sectoral stress from network context
5. **Ablation**: Compare GNN (with network) vs. models without network
6. **Output**: Test set performance vs. baseline models

**Tools**: `torch_geometric`, `PyTorch`

---

### Epic 3.4: Model Evaluation
**Goal**: Comprehensive comparison

*Code steps:*
1. **Metrics table**: RMSE, MAE, MAPE, R² for all models
2. **Prediction plots**: Actual vs. predicted for 5 sample sectors
3. **Error analysis**: When/where do models fail? (recession periods? specific sectors?)
4. **Statistical tests**: Diebold-Mariano test (model A better than B?)
5. **Residuals**: Check for autocorrelation, heteroskedasticity
6. **Output**: Comparison tables + diagnostic plots

**Tools**: `matplotlib`, `statsmodels` (diagnostic tests)

---

### Epic 3.5: Scenario Simulation & Vulnerability
**Goal**: Answer policy questions

*Code steps:*

**Historical scenarios:**
1. Simulate 2008 crisis: replay actual commodity prices on current India
2. Simulate 2014 oil crash: same approach
3. Simulate 2022 Ukraine war: multi-commodity shock

**Policy interventions:**
4. Diversify energy imports: reduce Gulf oil share by 30%, see impact
5. Strategic petroleum reserve: buffer absorbs 10% of price shocks
6. Hedging via futures: reduce volatility

**Vulnerability ranking:**
7. Calculate index = exposure × network_centrality × price_volatility
8. Rank sectors: which 10 are most vulnerable?
9. **Output**: Scenario comparison graphs + top 10 vulnerable sectors list + policy recommendations

**Tools**: `pandas` (scenario manipulation), `matplotlib` (visualization)

---

## File Structure
```
project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_iv_analysis.ipynb
│   ├── 03_scm.ipynb
│   ├── 04_var_granger.ipynb
│   ├── 05_feature_engineering.ipynb
│   ├── 06_lstm.ipynb
│   ├── 07_xgboost.ipynb
│   ├── 08_gnn.ipynb
│   ├── 09_scenarios.ipynb
│   └── 10_final_report.ipynb
├── scripts/
│   ├── data_pipeline.py
│   ├── causal_analysis.py
│   ├── feature_engineering.py
│   ├── model_training.py
│   └── scenarios.py
├── results/
│   ├── tables/
│   └── plots/
└── README.md
```

---

## Team Task Breakdown

| Task | Team Member | Tools | Output |
|------|-------------|-------|--------|
| Data prep + EDA | Data Engineer | pandas, numpy | Clean master dataset |
| IV + Granger | Econometrician | statsmodels, linearmodels | Causal coefficients, tables |
| SCM | Causal Inference Specialist | synth_id, cvxpy | Counterfactual graphs |
| Feature engineering | ML Engineer | sklearn, pandas | 150→50 features |
| LSTM + XGBoost | ML Engineer | TensorFlow, xgboost | Predictions, comparison table |
| GNN | Deep Learning Specialist | PyTorch Geometric | Network-aware predictions |
| Scenarios + Visualization | Analytics/Data Viz | matplotlib, seaborn | Policy recommendations |
