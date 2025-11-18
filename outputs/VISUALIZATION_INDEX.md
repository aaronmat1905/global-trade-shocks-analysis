# 📊 Visualization Quick Index

**Quick reference guide to all project visualizations**

---

## 🎯 Start Here

### **Primary Analysis Tool**
👉 **[trade_network_dashboard.html](visualizations/Sprint2_1/trade_network_dashboard.html)** - Interactive 3D sectoral network (131 Indian sectors)

---

## 📁 By Category

### 🌐 Network Analysis

| Visual | Description | Type | Location |
|--------|-------------|------|----------|
| **Trade Network Dashboard** | Interactive 3D network with 131 sectors | HTML | `Sprint2_1/trade_network_dashboard.html` |
| Bottleneck Vulnerability | Heatmap of critical sectors | PNG | `Sprint2_1/bottleneck_vulnerability_map.png` |
| Dynamic Centrality | Centrality evolution over time | PNG | `Sprint2_1/dynamic_centrality_analysis.png` |
| Resilience Curves | Network robustness analysis | PNG | `Sprint2_1/network_resilience_curves.png` |
| Shortest Paths | Shock propagation pathways | PNG | `Sprint2_1/shortest_path_example.png` |
| Shock Simulation | Impact heatmap across sectors | PNG | `Sprint2_1/shock_simulation_heatmap.png` |

### 📈 Econometric Analysis

| Visual | Description | Type | Location |
|--------|-------------|------|----------|
| F-Statistics | Instrument strength validation | PNG | `Sprint2_1/first_stage_f_statistics.png` |
| ONI Instrument | Climate instrument visualization | PNG | `Sprint2_1/oni_instrument_visualization.png` |
| ONI vs Prices | First-stage IV relationship | PNG | `Sprint2_1/oni_vs_prices_scatter.png` |
| Multiplier Waterfall | Interactive multiplier decomposition | HTML | `Sprint2_1/multiplier_waterfall.html` |

### 🤖 Machine Learning Features

| Visual | Description | Type | Location |
|--------|-------------|------|----------|
| Correlation Matrix | Feature correlations | PNG | `Sprint2_1/feature_engineering/correlation_matrix.png` |
| Feature Importance | Random Forest rankings | PNG | `Sprint2_1/feature_engineering/feature_importance_rf.png` |
| Train/Test Split | Temporal data division | PNG | `Sprint2_1/feature_engineering/train_test_split.png` |

### 🎯 Causal ML Analysis

| Visual | Description | Type | Location |
|--------|-------------|------|----------|
| CATE Features | Treatment heterogeneity drivers | PNG | `sprint2_2/figurescate_feature_importance.png` |
| Meta-Learner Compare | Model performance comparison | PNG | `sprint2_2/figuresmeta_learner_comparison.png` |
| Policy Targeting | Optimal intervention design | PNG | `sprint2_2/figurespolicy_targeting_analysis.png` |
| Vulnerability Comprehensive | Integrated vulnerability assessment | PNG | `sprint2_2/figuresvulnerability_comprehensive.png` |

---

## 🎓 By Use Case

### For Presentations

**Essential Figures (5-slide deck):**
1. `trade_network_dashboard.html` - Interactive demo
2. `bottleneck_vulnerability_map.png` - Problem statement
3. `first_stage_f_statistics.png` - Methodology
4. `shock_simulation_heatmap.png` - Main results
5. `figurespolicy_targeting_analysis.png` - Policy implications

**Extended Presentation (10+ slides):** Add
- `oni_instrument_visualization.png`
- `network_resilience_curves.png`
- `figuresmeta_learner_comparison.png`
- `multiplier_waterfall.html`

### For Research Papers

**Main Text Figures:**
1. `shock_simulation_heatmap.png` - Primary results
2. `first_stage_f_statistics.png` - IV validation
3. `figuresmeta_learner_comparison.png` - Methods
4. `bottleneck_vulnerability_map.png` - Network insights

**Appendix/Supplementary:**
- `oni_vs_prices_scatter.png`
- `correlation_matrix.png`
- `train_test_split.png`
- `network_resilience_curves.png`

### For Policy Briefs

**Executive Summary:**
1. `trade_network_dashboard.html` - Interactive exploration
2. `figuresvulnerability_comprehensive.png` - Vulnerability overview
3. `figurespolicy_targeting_analysis.png` - Recommendations

**Technical Annex:**
- `shock_simulation_heatmap.png`
- `bottleneck_vulnerability_map.png`
- `first_stage_f_statistics.png`

---

## 📊 By Analysis Type

### Descriptive Analysis
- ✅ `trade_network_dashboard.html`
- ✅ `bottleneck_vulnerability_map.png`
- ✅ `dynamic_centrality_analysis.png`
- ✅ `shortest_path_example.png`

### Causal Inference
- ✅ `first_stage_f_statistics.png`
- ✅ `oni_instrument_visualization.png`
- ✅ `oni_vs_prices_scatter.png`

### Predictive Modeling
- ✅ `correlation_matrix.png`
- ✅ `feature_importance_rf.png`
- ✅ `train_test_split.png`

### Counterfactual Analysis
- ✅ `shock_simulation_heatmap.png`
- ✅ `network_resilience_curves.png`
- ✅ `multiplier_waterfall.html`

### Treatment Effects
- ✅ `figurescate_feature_importance.png`
- ✅ `figuresmeta_learner_comparison.png`
- ✅ `figurespolicy_targeting_analysis.png`

---

## 🚀 Quick Access Paths

### Interactive Dashboards
```
outputs/visualizations/Sprint2_1/
├── trade_network_dashboard.html         ⭐ PRIMARY
├── multiplier_waterfall.html
├── network_3d_visualization.html
├── network_3d_visualization_enhanced.html
└── network_3d_dashboard_final.html
```

### Static Visualizations - Sprint 2.1
```
outputs/visualizations/Sprint2_1/
├── bottleneck_vulnerability_map.png
├── dynamic_centrality_analysis.png
├── first_stage_f_statistics.png
├── network_resilience_curves.png
├── oni_instrument_visualization.png
├── oni_vs_prices_scatter.png
├── shock_simulation_heatmap.png
├── shortest_path_example.png
└── feature_engineering/
    ├── correlation_matrix.png
    ├── feature_importance_rf.png
    └── train_test_split.png
```

### Static Visualizations - Sprint 2.2
```
outputs/visualizations/sprint2_2/
├── figurescate_feature_importance.png
├── figuresmeta_learner_comparison.png
├── figurespolicy_targeting_analysis.png
└── figuresvulnerability_comprehensive.png
```

---

## 🎨 Visualization Types

### 📊 Charts & Graphs (8)
- Bar charts: F-statistics, Feature importance, CATE importance
- Line charts: Dynamic centrality, Resilience curves
- Scatter plots: ONI vs Prices
- Waterfall: Multiplier decomposition

### 🗺️ Heatmaps & Matrices (3)
- Bottleneck vulnerability map
- Shock simulation heatmap
- Correlation matrix

### 🌐 Networks (5)
- 3D interactive network (4 versions)
- Shortest path visualization

### 📈 Multi-Panel (3)
- Meta-learner comparison
- Policy targeting analysis
- Vulnerability comprehensive

### 📉 Other (1)
- Train/test split timeline

---

## 💡 Tips & Best Practices

### Opening Files

**HTML Dashboards:**
```bash
# Windows
start outputs/visualizations/Sprint2_1/trade_network_dashboard.html

# Mac/Linux
open outputs/visualizations/Sprint2_1/trade_network_dashboard.html
```

**PNG Images:**
- Use any image viewer
- Recommended: Preview (Mac), Photos (Windows), GIMP (editing)

### Embedding in Documents

**PowerPoint/Keynote:**
1. Insert → Picture → Choose PNG file
2. Recommended size: Full slide width
3. Maintain aspect ratio

**LaTeX:**
```latex
\begin{figure}[h]
\centering
\includegraphics[width=0.8\textwidth]{outputs/visualizations/Sprint2_1/shock_simulation_heatmap.png}
\caption{Shock Simulation Heatmap}
\label{fig:shock_sim}
\end{figure}
```

**Word/Google Docs:**
1. Insert → Image → Upload PNG
2. Wrap text: In line with text or Wrap text
3. Add caption below

### Exporting Dashboard Screenshots

**From Browser:**
1. Open `trade_network_dashboard.html`
2. Click camera icon in Plotly toolbar
3. Or use browser screenshot (F12 → Screenshot)
4. Save as PNG (1920x1080 recommended)

---

## 📏 Technical Specifications

### Image Files

| File | Dimensions | DPI | Size | Format |
|------|-----------|-----|------|--------|
| PNG files | Variable | 300+ | 50-500KB | PNG |
| HTML files | Responsive | Vector | 85KB-5MB | HTML5 |

### Browser Requirements

**Interactive Dashboards:**
- Chrome/Edge: ✅ Recommended
- Firefox: ✅ Supported
- Safari: ✅ Supported
- IE: ❌ Not supported

**Internet Required:**
- For CDN libraries (Plotly, Font Awesome)
- Files work offline after initial load
- Dashboard caches in browser

---

## 🔄 Regeneration Commands

### All Visualizations
```python
# Sprint 2.1
python scripts/sprint2_1_analysis.py

# Sprint 2.2
python scripts/sprint2_2_causalml.py
```

### Dashboard Only
```python
cd outputs/visualizations/Sprint2_1/
python create_annotated_dashboard.py
```

### Individual Figures
```python
# Network analysis
python scripts/generate_network_visualizations.py

# Econometric
python scripts/generate_iv_diagnostics.py

# Causal ML
python scripts/generate_causalml_figures.py
```

---

## 📚 Related Documentation

- **[VISUALIZATION_CATALOG.md](VISUALIZATION_CATALOG.md)** - Comprehensive documentation
- **[SECTOR_ANALYSIS_GUIDE.md](visualizations/Sprint2_1/SECTOR_ANALYSIS_GUIDE.md)** - Network analysis guide
- **[DASHBOARD_GUIDE.md](visualizations/Sprint2_1/DASHBOARD_GUIDE.md)** - Dashboard features
- **[QUICK_START.md](visualizations/Sprint2_1/QUICK_START.md)** - Quick reference

---

## 🆘 Common Issues

**Dashboard won't load:**
- Check internet connection (for CDN)
- Clear browser cache
- Try different browser
- File size ~5MB may take 2-3 seconds

**Images appear blurry:**
- Check DPI (should be 300+)
- Don't resize in PowerPoint (maintain aspect ratio)
- Use vector formats when available

**Can't find a sector:**
- Use search box in dashboard
- Check spelling
- Try category filter
- All 131 sectors are included

---

## 📊 Statistics

| Metric | Count |
|--------|-------|
| Total visualizations | 20 |
| PNG images | 16 |
| HTML interactive | 4 |
| Network visualizations | 5 |
| Econometric figures | 4 |
| ML/Feature figures | 3 |
| Causal ML figures | 4 |
| Total size | ~6-8 MB |

---

**Last Updated:** November 2025
**Quick Access Version:** 1.0
**Status:** Ready ✓

---

## 🔗 Quick Links

[📖 Full Catalog](VISUALIZATION_CATALOG.md) | [🌐 Main Dashboard](visualizations/Sprint2_1/trade_network_dashboard.html) | [📊 Project README](../README.md)
