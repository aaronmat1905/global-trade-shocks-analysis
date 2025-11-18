# 🚀 Quick Start Guide - Enhanced Network Dashboard

## 📂 File to Open
**`network_3d_dashboard_final.html`** ← Open this in your browser!

## 🎯 Quick Actions

### Essential Controls
| Action | How To |
|--------|--------|
| Rotate View | Click & Drag |
| Zoom In/Out | Scroll Wheel |
| Select Node | Click on any node |
| Reset Camera | Click "Reset View" button |

### Layout Options (Left Sidebar)
```
📊 Layout Type
├─ 3D Force-Directed (Default)
├─ Circular
├─ Hierarchical
└─ Radial

🎨 Visual Controls
├─ Node Size: 2 ━━━━○━━━━━ 20
├─ Edge Width: 0.1 ━━○━━━━━ 5
└─ Edge Opacity: 0 ━━━○━━━━ 1

🌈 Color Schemes
├─ Default
├─ By Sector
├─ By Centrality
└─ By Community

🔍 Search & Filter
└─ Type to find nodes...

⚙️ Display Options
├─ [✓] Node Labels
├─ [✓] Show Edges
├─ [ ] Grid Lines
└─ [ ] Auto Rotate
```

### View Shortcuts (Center Panel)
```
🎥 Camera Views
├─ [🧊] 3D View
├─ [⬍] Top View
├─ [⬌] Side View
└─ [👁] Front View
```

### Statistics (Right Sidebar)
```
📈 Network Metrics
├─ Total Nodes: ###
├─ Total Edges: ###
├─ Network Density: 0.###
└─ Avg. Degree: ##.##

⭐ Top Nodes
├─ Node A ━━━━━━━━━ 85%
├─ Node B ━━━━━━━━ 72%
├─ Node C ━━━━━━ 68%
└─ Node D ━━━━ 54%

ℹ️ Selected Node Info
└─ Click any node to view details
```

## 💡 Pro Tips

### Best Viewing Experience
1. Use full screen (F11)
2. Adjust node size to ~10
3. Set edge opacity to 0.3
4. Enable auto-rotate for presentations

### Performance Optimization
- Disable node labels for large networks
- Reduce edge opacity for better visibility
- Use view presets instead of manual rotation

### Data Exploration
1. Search for specific nodes by name
2. Click nodes to see detailed stats
3. Compare top nodes by centrality
4. Monitor network density metric

## 🎨 Color Meanings

**Default Scheme:**
- Colors represent different communities
- Warmer colors = Higher values
- Cooler colors = Lower values

**By Centrality:**
- Red = High centrality (important nodes)
- Blue = Low centrality (peripheral nodes)

## 📸 Export Options

### Screenshot
- Click camera icon in Plotly toolbar
- Saves as PNG (1920x1080)

### Data Export
- Click "Export Data" button in header
- Downloads JSON with all network data

## 🔧 Common Adjustments

### Too Cluttered?
```
✓ Reduce edge opacity → 0.1-0.2
✓ Disable node labels
✓ Increase node size for focus
```

### Can't See Connections?
```
✓ Increase edge width → 1.5-2
✓ Increase edge opacity → 0.5-0.7
✓ Use darker background
```

### Need Better Overview?
```
✓ Switch to "Top View"
✓ Zoom out (scroll down)
✓ Enable grid lines
```

## ⌨️ Keyboard Shortcuts (Plotly)

| Key | Action |
|-----|--------|
| Double Click | Reset to home view |
| Shift + Drag | Pan view |
| Scroll | Zoom in/out |

## 🆘 Troubleshooting

**Dashboard won't load?**
- Check internet connection (loads CDN libraries)
- Use modern browser (Chrome, Firefox, Edge)
- Clear browser cache

**Slow performance?**
- Close other browser tabs
- Reduce node count via filtering
- Disable auto-rotate

**Can't find a node?**
- Use search box in left sidebar
- Check spelling
- Try partial name match

## 📊 Dashboard Layout

```
┌─────────────────────────────────────────────────────┐
│  🌐 Global Trade Network - Dashboard      🔄 📥    │
├──────────┬──────────────────────────┬───────────────┤
│          │                          │               │
│ Controls │    3D Visualization      │  Statistics   │
│          │                          │               │
│ • Layout │    [Network Graph]       │  • Metrics    │
│ • Visual │                          │  • Rankings   │
│ • Colors │    🎥 View Controls      │  • Node Info  │
│ • Search │                          │               │
│ • Toggle │                          │               │
│          │                          │               │
└──────────┴──────────────────────────┴───────────────┘
  (300px)         (flexible)              (320px)
```

## 🎯 Use Cases

**Network Analysis:**
1. Identify central nodes (hubs)
2. Detect communities/clusters
3. Analyze connectivity patterns
4. Find isolated nodes

**Presentations:**
1. Enable auto-rotate
2. Switch to full screen
3. Use view presets for impact
4. Capture screenshots

**Data Exploration:**
1. Filter by search terms
2. Compare node metrics
3. Track edge patterns
4. Export for further analysis

---

**Ready to Start?** Open `network_3d_dashboard_final.html` and explore! 🚀
