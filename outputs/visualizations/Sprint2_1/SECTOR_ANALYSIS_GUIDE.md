# Global Trade Shocks - Sectoral Network Analysis Dashboard

## Overview

This professional dashboard visualizes the **Indian economic sectoral network** for analyzing global trade shocks, supply chain vulnerabilities, and inter-sectoral dependencies.

## 📊 Your Data

### Network Composition
- **131 Economic Sectors** (nodes)
- **Inter-sectoral linkages** (edges representing input-output relationships)
- **12 Major Categories** grouping related sectors

### Sector Categories

1. **Agriculture** (20 sectors)
   - Paddy, Wheat, Rice, Cotton, Tea, Coffee, Rubber, etc.

2. **Livestock & Food** (13 sectors)
   - Poultry, Milk products, Fishing, Sugar, Edible oils, Beverages, etc.

3. **Textiles & Apparel** (10 sectors)
   - Cotton textiles, Jute textiles, Silk, Woolen, Ready-made garments, etc.

4. **Chemicals** (11 sectors)
   - Fertilizers, Drugs & medicine, Pesticides, Plastics, Paints, etc.

5. **Mining & Energy** (13 sectors)
   - Coal, Petroleum, Natural Gas, Iron ore, Electricity, etc.

6. **Metals & Manufacturing** (9 sectors)
   - Iron & steel, Cement, Metal products, etc.

7. **Machinery & Equipment** (10 sectors)
   - Industrial machinery, Electrical equipment, Electronics, etc.

8. **Transport Equipment** (8 sectors)
   - Motor vehicles, Aircraft, Ships, Railway equipment, etc.

9. **Services** (19 sectors)
   - Trade, Hotels, Transport, Financial services, Education, Healthcare, etc.

10. **Infrastructure & Utilities** (4 sectors)
    - Construction, Water supply, Public administration, etc.

11. **Other Industries** (12 sectors)
    - Wood products, Paper, Leather, Furniture, Jewelry, etc.

12. **Other** (2 sectors)
    - Miscellaneous sectors

## 🎯 Dashboard Features

### Main File
**`trade_network_dashboard.html`** ← **OPEN THIS FILE**

### What You'll See

#### Left Panel - Network Information
- **About Dataset**: Context about the sectoral network
- **Network Structure**: How to interpret nodes and edges
- **Category Filter**: Filter by sector category
- **Search**: Find specific sectors by name
- **Instructions**: How to interact with the visualization

#### Center Panel - 3D Visualization
- **Interactive 3D Network**:
  - Each **node** = one economic sector
  - Each **edge** = input-output relationship/trade linkage
  - **Colors** = sector categories
  - **Size** = number of connections (degree centrality)

#### Right Panel - Statistics & Analysis
- **Total Sectors**: 131 economic sectors
- **Total Linkages**: Inter-sectoral connections
- **Network Density**: How interconnected the economy is
- **Category Breakdown**: Sectors per category
- **Selected Sector Info**: Click any sector to see details

## 🔍 Use Cases

### 1. Trade Shock Analysis
**Identify vulnerable sectors:**
- Look for highly connected nodes (large size)
- These are sectors that affect many others
- Shocks here propagate widely through the economy

### 2. Supply Chain Mapping
**Understand dependencies:**
- Click on a sector to see its connections
- Trace paths between sectors
- Identify critical intermediaries

### 3. Sectoral Clustering
**Find related sectors:**
- Colors show categorical groupings
- Spatial proximity shows trading relationships
- Identify industry clusters

### 4. Policy Impact Assessment
**Evaluate policy effects:**
- Select a sector (e.g., "Fertilizers")
- See all connected sectors
- Understand downstream/upstream impacts

### 5. Economic Structure Analysis
**Analyze economy composition:**
- View category distribution
- Identify dominant sectors
- Assess sectoral balance

## 📖 How to Use

### Basic Interaction
1. **Open** `trade_network_dashboard.html` in your browser
2. **Rotate**: Click and drag anywhere in the visualization
3. **Zoom**: Scroll wheel or pinch gesture
4. **Select**: Click on any sector node

### Finding Specific Sectors
1. Use the **Search box** (left panel)
2. Type sector name (e.g., "Agriculture", "Steel", "Trade")
3. Results highlight in the network

### Filtering by Category
1. Use the **Category Filter** dropdown
2. Select a category (e.g., "Services")
3. View only sectors in that category

### Viewing Details
1. **Click any sector node**
2. See in right panel:
   - Sector name
   - Category
   - Number of connections
3. Understand its importance in the network

### Changing Views
1. **3D View**: Full perspective (default)
2. **Top View**: Bird's eye view
3. **Side View**: Horizontal perspective
4. Use view buttons in center panel header

### Exporting Data
1. Click **"Export Data"** button (top right)
2. Downloads JSON file with:
   - All sector names
   - Categories
   - Connection counts
   - Network statistics

## 📈 Understanding the Visualization

### Node Properties
- **Position**: Determined by network layout algorithm
  - Similar sectors cluster together
  - Connected sectors are closer
- **Size**: Degree centrality (number of connections)
  - Larger = more connected = more central
  - Smaller = fewer connections = peripheral
- **Color**: Sector category
  - Same category = same color family
  - Use colorbar to identify categories

### Edge Properties
- **Lines between nodes**: Trade/input-output relationships
- **Opacity**: Reduced for clarity
- **No direction**: Undirected network (mutual relationships)

### Network Metrics

**Network Density**
- Ratio: (actual connections) / (possible connections)
- Higher = more interconnected economy
- Lower = more segmented economy

**Degree Centrality**
- Count of connections per sector
- High degree = critical hub
- Low degree = specialized/isolated

## 🔬 Analysis Insights

### Critical Sectors (High Connectivity)
Look for **large nodes** - these sectors:
- Have many input-output relationships
- Are central to the economy
- Amplify shocks (both positive and negative)
- Are policy leverage points

### Peripheral Sectors (Low Connectivity)
Look for **small nodes** - these sectors:
- Are more isolated
- Have fewer direct dependencies
- May be less affected by broad shocks
- Could be niche/specialized

### Sector Clusters
Look for **spatial groupings** - these indicate:
- Related industries
- Supply chain relationships
- Regional industrial complexes
- Trade corridors

## 💡 Research Applications

### For Trade Shock Analysis
1. Identify import-dependent sectors
2. Map shock propagation paths
3. Quantify cascade effects
4. Design resilience strategies

### For Policy Analysis
1. Target sectors for intervention
2. Estimate multiplier effects
3. Assess policy spillovers
4. Optimize resource allocation

### For Economic Forecasting
1. Model inter-sectoral dynamics
2. Predict growth patterns
3. Identify bottlenecks
4. Simulate scenarios

## 📊 Data Details

### Source
Input-Output table for Indian economy with 131 disaggregated sectors

### Network Type
- **Undirected**: Relationships are bidirectional
- **Weighted**: Edges represent transaction volumes
- **Spatial**: 3D layout for visualization clarity

### Categories Used
Sectors are categorized by:
- Industry type
- Production characteristics
- Economic function
- Policy relevance

## 🎨 Customization

The dashboard can be extended with:
- **Time series**: Animate network evolution
- **Weights**: Show edge thickness by transaction volume
- **Metrics**: Add betweenness, closeness centrality
- **Filters**: Multiple simultaneous filters
- **Comparison**: Compare pre/post shock states

## 🆘 Troubleshooting

**Dashboard won't load?**
- Ensure internet connection (loads CDN libraries)
- Use modern browser (Chrome, Firefox, Edge)
- File size is ~5MB, may take a few seconds

**Can't find a sector?**
- Check spelling in search box
- Try category filter instead
- All 131 sectors are included

**Visualization too cluttered?**
- Use category filter to show subset
- Zoom in on area of interest
- Hide edge lines (future feature)

## 📚 Related Files

- `extracted_network_data.json` - Raw data export
- `network_3d_visualization.html` - Original visualization
- `QUICK_START.md` - Quick reference guide
- `DASHBOARD_GUIDE.md` - General dashboard documentation

## 🎯 Next Steps

1. **Explore the network** - Click around, understand structure
2. **Identify key sectors** - Note large, central nodes
3. **Trace relationships** - Follow connections between sectors
4. **Export for analysis** - Download data for further research
5. **Document insights** - Note patterns for your analysis

---

**Dashboard Version:** 2.0
**Data:** Indian Economic Sectors (131 sectors)
**Created:** November 2025
**Purpose:** Global Trade Shocks Analysis
