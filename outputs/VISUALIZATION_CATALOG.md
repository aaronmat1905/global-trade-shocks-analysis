# Global Trade Shocks Analysis - Visualization Catalog

**Project:** Global Trade Shocks Analysis
**Output Directory:** `outputs/`
**Total Visualizations:** 20 files
**Last Updated:** November 2025

---

## 📊 Table of Contents

1. [Overview](#overview)
2. [Sprint 2.1 - Network & Econometric Analysis](#sprint-21---network--econometric-analysis)
3. [Sprint 2.2 - Causal Machine Learning](#sprint-22---causal-machine-learning)
4. [Interactive Dashboards](#interactive-dashboards)
5. [Usage Guide](#usage-guide)

---

## Overview

This catalog documents all visualization outputs generated during the Global Trade Shocks analysis project. Visualizations are organized by sprint and analysis type.

### Directory Structure

```
outputs/
├── csv_outputs/
│   └── causalML/              # CausalML results (CSV files)
└── visualizations/
    ├── Sprint2_1/              # Network & Econometric Analysis
    │   ├── feature_engineering/  # ML feature analysis
    │   └── *.png, *.html       # Main visualizations
    └── sprint2_2/              # Causal ML Analysis
        └── figures*.png        # CausalML visualizations
```

### File Types

- **PNG Images** (16 files) - Static publication-ready visualizations
- **HTML Interactive** (4 files) - Interactive 3D dashboards
- **Total Size** - Approximately 6-8 MB

---

## Sprint 2.1 - Network & Econometric Analysis

**Location:** `outputs/visualizations/Sprint2_1/`
**Count:** 16 files (12 PNG, 4 HTML)
**Focus:** Network analysis, instrumental variables, shock propagation

### 📈 Network Analysis Visualizations

#### 1. `bottleneck_vulnerability_map.png`
- **Type:** Network heatmap
- **Content:** Identifies bottleneck sectors and vulnerability hotspots
- **Analysis:** Shows which sectors act as critical nodes in the supply chain
- **Use Case:**
  - Identify systemic risk points
  - Target sectors for resilience building
  - Assess supply chain fragility
- **Key Insights:**
  - Darker colors = higher vulnerability
  - Size = importance in network
  - Position = clustering with related sectors

#### 2. `dynamic_centrality_analysis.png`
- **Type:** Time-series line chart
- **Content:** Evolution of sector centrality measures over time
- **Metrics Shown:**
  - Degree centrality
  - Betweenness centrality
  - Eigenvector centrality
- **Use Case:**
  - Track changing importance of sectors
  - Identify emerging hubs
  - Monitor structural shifts in economy
- **Key Insights:**
  - Trends show economy restructuring
  - Peaks indicate temporary importance shifts
  - Divergence shows structural changes

#### 3. `network_resilience_curves.png`
- **Type:** Multi-line chart
- **Content:** Network resilience under different shock scenarios
- **Scenarios:**
  - Random node failures
  - Targeted attacks on hubs
  - Cascading failures
- **Use Case:**
  - Assess network robustness
  - Compare resilience strategies
  - Plan crisis response
- **Key Insights:**
  - Steeper decline = less resilient
  - Compare curves for vulnerability assessment
  - Inflection points show critical thresholds

#### 4. `shortest_path_example.png`
- **Type:** Network diagram with highlighted paths
- **Content:** Illustrates shortest paths between sectors
- **Purpose:** Shows how shocks propagate through the network
- **Use Case:**
  - Understand shock transmission mechanisms
  - Identify critical intermediaries
  - Map dependencies
- **Key Insights:**
  - Path length = propagation time
  - Nodes on multiple paths = systemic importance
  - Clustered paths = concentrated risk

#### 5. `shock_simulation_heatmap.png`
- **Type:** Heatmap matrix
- **Content:** Simulated shock impacts across all sectors
- **Dimensions:**
  - Rows: Shock origin sectors
  - Columns: Affected sectors
  - Color: Impact magnitude
- **Use Case:**
  - Predict cascade effects
  - Identify vulnerable sector pairs
  - Design targeted interventions
- **Key Insights:**
  - Diagonal = direct impacts
  - Off-diagonal = spillover effects
  - Clusters show correlated vulnerabilities

### 📊 Econometric Analysis Visualizations

#### 6. `first_stage_f_statistics.png`
- **Type:** Bar chart with threshold line
- **Content:** F-statistics for instrumental variable validity
- **Instruments:** Oceanic Niño Index (ONI) and other climate variables
- **Threshold:** F > 10 (standard IV strength criterion)
- **Use Case:**
  - Validate instrument strength
  - Justify IV approach
  - Check weak instrument problem
- **Key Insights:**
  - Bars above line = strong instruments
  - Higher values = better identification
  - Compare across sectors/models

#### 7. `oni_instrument_visualization.png`
- **Type:** Time series with dual axes
- **Content:** ONI values and their correlation with trade variables
- **Components:**
  - Primary axis: ONI index
  - Secondary axis: Trade flows/prices
  - Correlation coefficient displayed
- **Use Case:**
  - Demonstrate instrument relevance
  - Show exogenous variation
  - Validate IV assumptions
- **Key Insights:**
  - Co-movement indicates relevance
  - Lag structure shows causality
  - Variance shows instrument strength

#### 8. `oni_vs_prices_scatter.png`
- **Type:** Scatter plot with regression line
- **Content:** Relationship between ONI and commodity prices
- **Elements:**
  - Points: Observations
  - Line: Fitted relationship
  - R² and p-value displayed
- **Use Case:**
  - First-stage IV regression visualization
  - Show reduced form relationship
  - Assess instrument-endogenous relationship
- **Key Insights:**
  - Slope = instrument strength
  - R² = explanatory power
  - Scatter = residual variance

#### 9. `multiplier_waterfall.html`
- **Type:** Interactive waterfall chart (HTML)
- **Content:** Decomposition of economic multiplier effects
- **Components:**
  - Direct effects
  - Indirect effects (by order)
  - Induced effects
  - Total multiplier
- **Use Case:**
  - Understand multiplier decomposition
  - Trace shock propagation stages
  - Quantify ripple effects
- **Interactions:**
  - Hover for exact values
  - Click to highlight stages
  - Zoom for detail
- **Key Insights:**
  - Width = magnitude of effect
  - Cumulative build-up visible
  - Compare direct vs. total impact

### 🤖 Feature Engineering Visualizations

**Location:** `outputs/visualizations/Sprint2_1/feature_engineering/`

#### 10. `correlation_matrix.png`
- **Type:** Heatmap correlation matrix
- **Content:** Correlations between engineered features
- **Features Include:**
  - Network metrics (centrality, clustering)
  - Structural characteristics
  - Trade intensities
  - Lag variables
- **Use Case:**
  - Feature selection
  - Multicollinearity detection
  - Variable importance ranking
- **Key Insights:**
  - Dark red/blue = strong correlation
  - Diagonal = 1.0 (self-correlation)
  - Off-diagonal clusters = redundant features

#### 11. `feature_importance_rf.png`
- **Type:** Horizontal bar chart
- **Content:** Random Forest feature importance scores
- **Ranking:** Top 20 most important features
- **Metric:** Mean decrease in impurity / permutation importance
- **Use Case:**
  - Identify key predictors
  - Validate economic theory
  - Guide model simplification
- **Key Insights:**
  - Longer bars = more important
  - Network metrics vs. traditional variables
  - Unexpected features for investigation

#### 12. `train_test_split.png`
- **Type:** Time series split visualization
- **Content:** Shows temporal division of data
- **Components:**
  - Training period (blue)
  - Validation period (orange)
  - Test period (green)
  - Time markers
- **Use Case:**
  - Verify temporal consistency
  - Ensure no data leakage
  - Document methodology
- **Key Insights:**
  - No overlap = valid split
  - Proportions shown
  - Critical events marked

### 🌐 Interactive 3D Network Dashboards

#### 13. `trade_network_dashboard.html` ⭐ **RECOMMENDED**
- **Type:** Interactive 3D network dashboard
- **Size:** ~423 KB
- **Content:** Full sectoral network with annotations
- **Sectors:** 131 Indian economic sectors
- **Categories:** 12 major sector groups
- **Features:**
  - **Left Panel:** Network info, filters, search
  - **Center:** Interactive 3D visualization
  - **Right Panel:** Statistics, category breakdown
- **Interactions:**
  - Click sectors for details
  - Drag to rotate
  - Scroll to zoom
  - Search by name
  - Filter by category
- **Use Case:**
  - Primary analysis tool
  - Presentation to stakeholders
  - Exploratory analysis
  - Publication-ready visualization
- **Key Features:**
  - Real sector names (not generic labels)
  - Category color coding
  - Connection metrics
  - Export functionality

#### 14. `network_3d_visualization.html`
- **Type:** Basic 3D network (original)
- **Size:** ~5 MB (includes full Plotly library)
- **Content:** Raw Plotly visualization
- **Purpose:** Original generated output
- **Note:** Use `trade_network_dashboard.html` instead for analysis

#### 15. `network_3d_visualization_enhanced.html`
- **Type:** Enhanced template with sample data
- **Size:** ~85 KB
- **Content:** Dashboard template for testing
- **Purpose:** Development/template version
- **Note:** Contains sample data, not real sectors

#### 16. `network_3d_dashboard_final.html`
- **Type:** Dashboard with data extraction attempt
- **Size:** ~425 KB
- **Content:** Alternative dashboard version
- **Purpose:** Backup version
- **Note:** May have incomplete data loading

---

## Sprint 2.2 - Causal Machine Learning

**Location:** `outputs/visualizations/sprint2_2/`
**Count:** 4 files (all PNG)
**Focus:** Heterogeneous treatment effects, policy targeting, causal inference

### 🎯 Causal ML Visualizations

#### 17. `figurescate_feature_importance.png`
- **Type:** Horizontal bar chart
- **Content:** Feature importance from CATE (Conditional Average Treatment Effect) models
- **Models:**
  - S-Learner
  - T-Learner
  - X-Learner
  - Causal Forest
- **Use Case:**
  - Identify heterogeneity drivers
  - Understand treatment effect variation
  - Guide personalized policy design
- **Key Insights:**
  - Top features drive treatment heterogeneity
  - Compare across meta-learners
  - Validate with economic intuition

#### 18. `figuresmeta_learner_comparison.png`
- **Type:** Multi-panel comparison chart
- **Content:** Performance metrics across meta-learners
- **Metrics:**
  - CATE estimation accuracy
  - Confidence interval width
  - Out-of-sample performance
  - Computational time
- **Meta-Learners Compared:**
  - S-Learner (single model)
  - T-Learner (two models)
  - X-Learner (cross-fitting)
  - Causal Forest
  - DR-Learner (doubly robust)
- **Use Case:**
  - Select best meta-learner
  - Understand trade-offs
  - Justify methodological choice
- **Key Insights:**
  - Best performer highlighted
  - Trade-off between accuracy and complexity
  - Robustness across specifications

#### 19. `figurespolicy_targeting_analysis.png`
- **Type:** Multi-panel visualization
- **Content:** Optimal policy targeting based on CATE estimates
- **Panels:**
  - CATE distribution
  - Treatment effect heterogeneity
  - Optimal targeting threshold
  - Expected gains from targeting
- **Use Case:**
  - Design targeted interventions
  - Maximize policy efficiency
  - Identify high-impact subgroups
- **Key Insights:**
  - Treat above threshold
  - Quantify gains from targeting
  - Show treatment effect variation

#### 20. `figuresvulnerability_comprehensive.png`
- **Type:** Comprehensive multi-panel dashboard
- **Content:** Integrated vulnerability assessment
- **Components:**
  - Vulnerability scores by sector
  - Geographic/category clustering
  - Temporal evolution
  - Risk factors breakdown
- **Use Case:**
  - Holistic vulnerability assessment
  - Strategic planning
  - Resource allocation
  - Risk management
- **Key Insights:**
  - Multi-dimensional vulnerability
  - Spatial patterns
  - Time trends
  - Component contributions

---

## Interactive Dashboards

### Primary Dashboard: `trade_network_dashboard.html`

**Path:** `outputs/visualizations/Sprint2_1/trade_network_dashboard.html`

#### Features Overview

| Feature | Description |
|---------|-------------|
| **Sectors** | 131 Indian economic sectors with real names |
| **Categories** | 12 major groupings (Agriculture, Services, etc.) |
| **Interactions** | Click, drag, zoom, search, filter |
| **Statistics** | Real-time network metrics |
| **Export** | JSON data export capability |
| **Views** | 3D, Top, Side perspectives |
| **Search** | Find sectors by name |
| **Filter** | View by category |

#### Dashboard Layout

```
┌─────────────────────────────────────────────────────────────────┐
│ HEADER: Global Trade Shocks - Sectoral Network Analysis        │
├──────────────┬──────────────────────────┬───────────────────────┤
│              │                          │                       │
│ LEFT PANEL   │   CENTER: 3D NETWORK     │   RIGHT PANEL        │
│              │                          │                       │
│ • About      │   Interactive Graph      │   • Statistics       │
│ • Filter     │   - Drag to rotate       │   • 131 Sectors      │
│ • Search     │   - Scroll to zoom       │   • Linkages         │
│ • Guide      │   - Click for info       │   • Density          │
│              │                          │   • Categories       │
│              │   [3D] [Top] [Side]      │   • Sector Info      │
│              │                          │                       │
└──────────────┴──────────────────────────┴───────────────────────┘
```

#### Sector Categories

1. **Agriculture** (20) - Paddy, Wheat, Cotton, Tea, Coffee
2. **Livestock & Food** (13) - Dairy, Poultry, Sugar, Beverages
3. **Textiles & Apparel** (10) - Cotton, Jute, Silk, Garments
4. **Chemicals** (11) - Fertilizers, Pharma, Plastics
5. **Mining & Energy** (13) - Coal, Oil, Gas, Electricity
6. **Metals & Manufacturing** (9) - Steel, Cement, Metal products
7. **Machinery & Equipment** (10) - Industrial, Electrical, Electronics
8. **Transport Equipment** (8) - Vehicles, Aircraft, Ships
9. **Services** (19) - Trade, Finance, Transport, Education
10. **Infrastructure** (4) - Construction, Water, Public admin
11. **Other Industries** (12) - Paper, Leather, Furniture
12. **Other** (2) - Miscellaneous

#### Usage Instructions

**Opening the Dashboard:**
```bash
# Navigate to the file and open in browser
cd outputs/visualizations/Sprint2_1/
# Open trade_network_dashboard.html
```

**Basic Interactions:**
- **Rotate:** Click and drag anywhere
- **Zoom:** Scroll wheel or pinch
- **Select:** Click any sector node
- **Search:** Type sector name in search box
- **Filter:** Select category from dropdown
- **Export:** Click "Export Data" button

**Advanced Features:**
- **View Presets:** Use buttons for 3D, Top, Side views
- **Reset:** Click "Reset View" to return to default
- **Details:** Click sector to see connections and category
- **Statistics:** Auto-calculated in right panel

---

## Usage Guide

### For Researchers

#### Publication-Ready Figures

**Best Practices:**
1. **PNG files** are publication-ready at 300+ DPI
2. **Recommended figures for papers:**
   - `shock_simulation_heatmap.png` - Main results
   - `first_stage_f_statistics.png` - IV validation
   - `figuresmeta_learner_comparison.png` - Causal ML methods
   - `bottleneck_vulnerability_map.png` - Network insights

3. **Figure captions:** See individual descriptions above

#### Interactive Analysis

**Primary Tool:** `trade_network_dashboard.html`

**Workflow:**
1. Open dashboard in browser
2. Explore sector relationships
3. Filter by category for focused analysis
4. Click sectors to examine connections
5. Export data for further analysis
6. Take screenshots for presentations

### For Policy Makers

#### Key Visualizations for Decision Making

1. **Vulnerability Assessment:**
   - `bottleneck_vulnerability_map.png`
   - `figuresvulnerability_comprehensive.png`
   - `network_resilience_curves.png`

2. **Policy Targeting:**
   - `figurespolicy_targeting_analysis.png`
   - `shock_simulation_heatmap.png`
   - Interactive dashboard for sector exploration

3. **Methodology Validation:**
   - `first_stage_f_statistics.png`
   - `oni_instrument_visualization.png`
   - `figuresmeta_learner_comparison.png`

### For Presentations

#### Recommended Sequence

**15-Minute Presentation:**
1. **Intro:** `trade_network_dashboard.html` (interactive demo)
2. **Problem:** `bottleneck_vulnerability_map.png`
3. **Method:** `first_stage_f_statistics.png`
4. **Results:** `shock_simulation_heatmap.png`
5. **Policy:** `figurespolicy_targeting_analysis.png`
6. **Conclusion:** `network_resilience_curves.png`

**30-Minute Presentation:** Add
- `oni_instrument_visualization.png` (methodology)
- `figuresmeta_learner_comparison.png` (robustness)
- `multiplier_waterfall.html` (mechanism)

### For Technical Documentation

#### Methodology Figures

**Econometric Approach:**
- `first_stage_f_statistics.png` - IV strength
- `oni_instrument_visualization.png` - Instrument validity
- `oni_vs_prices_scatter.png` - First stage relationship

**Machine Learning:**
- `feature_importance_rf.png` - Variable selection
- `correlation_matrix.png` - Feature engineering
- `train_test_split.png` - Validation approach

**Causal Inference:**
- `figurescate_feature_importance.png` - Heterogeneity drivers
- `figuresmeta_learner_comparison.png` - Method comparison
- `figurespolicy_targeting_analysis.png` - Application

---

## File Management

### Backup Recommendations

**Critical Files (backup required):**
- `trade_network_dashboard.html` ⭐
- All PNG files in Sprint2_1/
- All PNG files in sprint2_2/

**Regenerable Files:**
- `network_3d_visualization.html` (can be regenerated)
- `network_3d_visualization_enhanced.html` (template)
- `network_3d_dashboard_final.html` (backup version)

### Version Control

**Current Structure:**
```
outputs/
├── visualizations/
│   ├── Sprint2_1/          # Version 2.1 (Nov 2025)
│   └── sprint2_2/          # Version 2.2 (Nov 2025)
└── csv_outputs/
    └── causalML/           # Supporting data
```

**Naming Convention:**
- Descriptive names (e.g., `shock_simulation_heatmap.png`)
- Sprint identifiers (e.g., `Sprint2_1/`, `sprint2_2/`)
- Feature prefixes (e.g., `figures*` for causal ML)

### Storage Requirements

**Total Size:** ~6-8 MB

**Breakdown:**
- PNG files: ~4 MB
- HTML dashboards: ~6 MB (includes Plotly library)
- Minimal storage footprint

---

## Maintenance & Updates

### Regenerating Visualizations

**Network Analysis:**
```python
# Run main analysis script
python scripts/sprint2_1_network_analysis.py
```

**Causal ML:**
```python
# Run causal ML analysis
python scripts/sprint2_2_causalml.py
```

**Interactive Dashboard:**
```python
# Regenerate annotated dashboard
cd outputs/visualizations/Sprint2_1/
python create_annotated_dashboard.py
```

### Quality Checks

**Image Quality:**
- ✓ All PNGs should be > 300 DPI
- ✓ Readable labels and legends
- ✓ Consistent color schemes
- ✓ Proper aspect ratios

**Interactive Dashboards:**
- ✓ Load in modern browsers (Chrome, Firefox, Edge)
- ✓ All controls functional
- ✓ Data properly displayed
- ✓ Export features working

### Known Issues

**Dashboard Loading:**
- Large HTML files (5MB) may take 2-3 seconds to load
- Ensure internet connection for CDN resources
- Use `trade_network_dashboard.html` for best performance

**Browser Compatibility:**
- Best viewed in Chrome/Edge
- Firefox and Safari supported
- IE not supported

---

## Documentation Files

### Related Documentation

| File | Description |
|------|-------------|
| `SECTOR_ANALYSIS_GUIDE.md` | Detailed guide to sectoral network |
| `DASHBOARD_GUIDE.md` | General dashboard features |
| `QUICK_START.md` | Quick reference guide |
| `VISUALIZATION_CATALOG.md` | This file |

### Project Documentation

**Main Documentation:**
- Project README in root directory
- Sprint-specific documentation in each sprint folder
- Code documentation in script headers

---

## Quick Reference

### File Location Quick Access

**Most Used Files:**
```bash
# Primary dashboard
outputs/visualizations/Sprint2_1/trade_network_dashboard.html

# Key analysis figures
outputs/visualizations/Sprint2_1/shock_simulation_heatmap.png
outputs/visualizations/Sprint2_1/bottleneck_vulnerability_map.png
outputs/visualizations/Sprint2_1/first_stage_f_statistics.png

# Causal ML results
outputs/visualizations/sprint2_2/figurespolicy_targeting_analysis.png
outputs/visualizations/sprint2_2/figuresmeta_learner_comparison.png
```

### Common Tasks

**View Network Dashboard:**
```bash
# Open in default browser
start outputs/visualizations/Sprint2_1/trade_network_dashboard.html  # Windows
open outputs/visualizations/Sprint2_1/trade_network_dashboard.html   # Mac
```

**Export All Figures:**
```bash
# Copy all visualizations
cp -r outputs/visualizations/ ~/presentation/
```

**Generate Figure List:**
```bash
# List all PNG files
find outputs/visualizations/ -name "*.png"
```

---

## Contact & Support

For questions about specific visualizations or to request new analyses:
- Review sprint-specific documentation
- Check code comments in generation scripts
- Refer to methodology documentation

---

**Last Updated:** November 2025
**Version:** 2.0
**Total Visualizations:** 20 files
**Status:** Production Ready ✓
