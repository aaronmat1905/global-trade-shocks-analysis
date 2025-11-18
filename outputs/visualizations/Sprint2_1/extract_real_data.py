"""
Extract real network data from the original visualization
and create an annotated dashboard for global trade shocks analysis
"""

import re
import json
from pathlib import Path

def extract_network_data(html_file):
    """Extract the complete network data from HTML"""
    print(f"Reading {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Plotly.newPlot section (it's near the end)
    plotly_start = content.find('Plotly.newPlot(')
    if plotly_start == -1:
        print("Could not find Plotly.newPlot")
        return None

    # Extract the data array
    # Looking for the pattern: Plotly.newPlot("div-id", [{...}, {...}], {...}, {...})

    # Find the opening bracket of the data array
    data_start = content.find('[', plotly_start)
    if data_start == -1:
        return None

    # Count brackets to find the matching close
    bracket_count = 1
    i = data_start + 1
    in_string = False
    escape = False

    while i < len(content) and bracket_count > 0:
        char = content[i]

        if escape:
            escape = False
            i += 1
            continue

        if char == '\\':
            escape = True
        elif char == '"':
            in_string = not in_string
        elif not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1

        i += 1

    data_json = content[data_start:i]

    print(f"Extracted {len(data_json)} characters of data")

    try:
        data = json.loads(data_json)
        print(f"Successfully parsed JSON with {len(data)} traces")
        return data
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        # Try to save the extracted string for debugging
        with open('debug_data.txt', 'w', encoding='utf-8') as f:
            f.write(data_json[:10000])
        return None

def categorize_sectors(node_names):
    """Categorize sectors into major groups"""
    categories = {
        'Agriculture': ['Paddy', 'Wheat', 'Gram', 'Pulses', 'Jowar', 'Bajra', 'Maize',
                       'Sugarcane', 'Groundnut', 'Coconut', 'Cotton', 'Jute', 'Tea',
                       'Coffee', 'Rubber', 'Tobacco', 'Vegetables', 'Fruits', 'Other crops',
                       'Other oilseeds'],
        'Livestock & Food': ['Poultry & Eggs', 'Milk and milk products', 'Other liv.st. produ.',
                            'Animal Services', 'Fishing & Aquaculture', 'Sugar', 'Edible oils',
                            'Grain Mill products', 'Beverages', 'Khandsari, boora',
                            'Hydrogenated oil', 'Miscellaneous food', 'Tea and coffee processing'],
        'Textiles & Apparel': ['Cotton textiles', 'Jute, hemp, mesta textiles',
                              'Art silk, synthetic fiber textiles', 'Woolen textiles',
                              'Silk textiles', 'Khadi, cotton textiles', 'Carpet weaving',
                              'Miscellaneous textile products', 'Ready made garments',
                              'Synthetic fibers, resin'],
        'Chemicals': ['Fertilizers', 'Organic heavy chemicals', 'Inorganic heavy chemicals',
                     'Drugs and medicine', 'Soaps, cosmetics & glycerin', 'Pesticides',
                     'Paints, varnishes', 'Other chemicals', 'Plastic products',
                     'Coal tar products', 'Rubber products'],
        'Mining & Energy': ['Coal and Lignite', 'Crude petroleum', 'Natural Gas', 'Iron ore',
                           'Bauxite', 'Manganese ore', 'Copper ore', 'Mica', 'Lime stone',
                           'Other Metallic minerals', 'Other non metallic minerals',
                           'Electricity', 'Petroleum products'],
        'Metals & Manufacturing': ['Iron, steel and ferro alloys', 'Iron and steel casting',
                                  'Iron and steel foundries', 'Non ferrous basic metals',
                                  'Cement', 'Miscellaneous metal products', 'Machine tools',
                                  'Hand tools, hardware', 'Batteries'],
        'Machinery & Equipment': ['Tractors and agri. implements', 'Industrial machinery',
                                  'Other non-electrical machinery', 'Electrical industrial Machinery',
                                  'Other electrical Machinery', 'Electronic equipments',
                                  'Communication equipment', 'Electrical wires & cables',
                                  'Electrical appliances', 'Medical, precision&optical instru.s'],
        'Transport Equipment': ['Motor vehicles', 'Motor cycles and scooters', 'Bicycles, cycle-rickshaw',
                               'Railway equipments', 'Ships and boats', 'Aircraft & spacecraft',
                               'Other transport equipments', 'Rail equipments'],
        'Services': ['Trade', 'Hotels & Restaurant', 'Railway Transport', 'Land transport',
                    'Water Transport', 'Air transport', 'Storage and warehousing',
                    'Supportive and Auxiliary transport activities', 'Communication services',
                    'Financial services', 'Insurance services', 'Real estate services',
                    'Renting of machinery', 'Computer related services', 'Legal services',
                    'Education and research', 'Medical and Health', 'Other Business services',
                    'Community, social and personal services', 'Other services'],
        'Infrastructure & Utilities': ['Construction and construction services', 'Water Supply',
                                      'Public administration and defence', 'Ownership of dwellings'],
        'Other Industries': ['Wood and wood products', 'Paper, Paper products', 'Leather and leather products',
                           'Leather footwear', 'Forestry and Logging', 'Publishing, printing',
                           'Furniture & Fixtures', 'Structural clay products',
                           'Other non-metallic mineral prods.', 'Jems & jewelry',
                           'Watches and clocks', 'Miscellaneous manufacturing']
    }

    sector_category = {}
    for node in node_names:
        found = False
        for category, keywords in categories.items():
            for keyword in keywords:
                if keyword.lower() in node.lower():
                    sector_category[node] = category
                    found = True
                    break
            if found:
                break
        if not found:
            sector_category[node] = 'Other'

    return sector_category

def create_annotated_dashboard(data, output_file):
    """Create dashboard HTML with real data and annotations"""

    if not data or len(data) < 2:
        print("Invalid data structure")
        return

    edge_trace = data[0]
    node_trace = data[1]

    node_names = node_trace.get('text', [])
    print(f"Found {len(node_names)} sectors")

    # Categorize sectors
    sector_categories = categorize_sectors(node_names)

    # Create category color mapping
    category_colors = {
        'Agriculture': 0,
        'Livestock & Food': 1,
        'Textiles & Apparel': 2,
        'Chemicals': 3,
        'Mining & Energy': 4,
        'Metals & Manufacturing': 5,
        'Machinery & Equipment': 6,
        'Transport Equipment': 7,
        'Services': 8,
        'Infrastructure & Utilities': 9,
        'Other Industries': 10,
        'Other': 11
    }

    # Count sectors by category
    category_counts = {}
    for category in category_colors.keys():
        category_counts[category] = sum(1 for c in sector_categories.values() if c == category)

    # Create the complete HTML with embedded data
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Global Trade Shocks - Sectoral Network Analysis Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-2.27.0.min.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        :root {{
            --primary-color: #2563eb;
            --secondary-color: #0ea5e9;
            --success-color: #10b981;
            --warning-color: #f59e0b;
            --danger-color: #ef4444;
            --dark-bg: #0f172a;
            --card-bg: #1e293b;
            --text-primary: #f1f5f9;
            --text-secondary: #94a3b8;
            --border-color: #334155;
            --shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.3), 0 2px 4px -1px rgba(0, 0, 0, 0.2);
        }}

        body {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: var(--text-primary);
            min-height: 100vh;
            overflow-x: hidden;
        }}

        /* Header */
        .header {{
            background: var(--card-bg);
            border-bottom: 1px solid var(--border-color);
            padding: 1rem 2rem;
            box-shadow: var(--shadow);
            position: sticky;
            top: 0;
            z-index: 1000;
        }}

        .header-content {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1920px;
            margin: 0 auto;
        }}

        .logo-section {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}

        .logo {{
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 1.5rem;
        }}

        .title-section h1 {{
            font-size: 1.5rem;
            font-weight: 700;
            background: linear-gradient(135deg, #60a5fa, #3b82f6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}

        .subtitle {{
            font-size: 0.875rem;
            color: var(--text-secondary);
            margin-top: 0.25rem;
        }}

        .header-actions {{
            display: flex;
            gap: 1rem;
            align-items: center;
        }}

        .btn {{
            padding: 0.5rem 1rem;
            border-radius: 8px;
            border: none;
            cursor: pointer;
            font-weight: 500;
            transition: all 0.3s ease;
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            font-size: 0.875rem;
        }}

        .btn-primary {{
            background: linear-gradient(135deg, var(--primary-color), var(--secondary-color));
            color: white;
        }}

        .btn-primary:hover {{
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3);
        }}

        .btn-secondary {{
            background: var(--card-bg);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
        }}

        .btn-secondary:hover {{
            background: var(--border-color);
        }}

        /* Main Layout */
        .dashboard-container {{
            display: grid;
            grid-template-columns: 320px 1fr 360px;
            gap: 1.5rem;
            padding: 1.5rem;
            max-width: 1920px;
            margin: 0 auto;
            height: calc(100vh - 80px);
        }}

        /* Sidebar */
        .sidebar {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: var(--shadow);
            overflow-y: auto;
            border: 1px solid var(--border-color);
        }}

        .sidebar h2 {{
            font-size: 1.125rem;
            margin-bottom: 1.5rem;
            color: var(--text-primary);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .info-box {{
            background: var(--dark-bg);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            border-left: 3px solid var(--primary-color);
        }}

        .info-box h3 {{
            font-size: 0.875rem;
            color: var(--primary-color);
            margin-bottom: 0.5rem;
            text-transform: uppercase;
            letter-spacing: 0.05em;
        }}

        .info-box p {{
            font-size: 0.875rem;
            color: var(--text-secondary);
            line-height: 1.5;
        }}

        .control-group {{
            margin-bottom: 1.5rem;
        }}

        .control-group label {{
            display: block;
            font-size: 0.875rem;
            font-weight: 500;
            margin-bottom: 0.5rem;
            color: var(--text-secondary);
        }}

        .control-group select,
        .control-group input[type="text"] {{
            width: 100%;
            padding: 0.625rem;
            background: var(--dark-bg);
            border: 1px solid var(--border-color);
            border-radius: 8px;
            color: var(--text-primary);
            font-size: 0.875rem;
            transition: all 0.3s ease;
        }}

        .control-group select:focus,
        .control-group input[type="text"]:focus {{
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
        }}

        /* Main Content */
        .main-content {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: var(--shadow);
            border: 1px solid var(--border-color);
            overflow: hidden;
            display: flex;
            flex-direction: column;
        }}

        .content-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}

        .content-header h2 {{
            font-size: 1.25rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .view-controls {{
            display: flex;
            gap: 0.5rem;
        }}

        .view-btn {{
            padding: 0.5rem;
            background: var(--dark-bg);
            border: 1px solid var(--border-color);
            border-radius: 6px;
            color: var(--text-secondary);
            cursor: pointer;
            transition: all 0.3s ease;
        }}

        .view-btn:hover,
        .view-btn.active {{
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }}

        #networkPlot {{
            flex: 1;
            border-radius: 8px;
            overflow: hidden;
        }}

        /* Right Sidebar - Stats */
        .stats-panel {{
            background: var(--card-bg);
            border-radius: 12px;
            padding: 1.5rem;
            box-shadow: var(--shadow);
            overflow-y: auto;
            border: 1px solid var(--border-color);
        }}

        .stats-panel h2 {{
            font-size: 1.125rem;
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}

        .stat-card {{
            background: var(--dark-bg);
            border-radius: 8px;
            padding: 1rem;
            margin-bottom: 1rem;
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }}

        .stat-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        }}

        .stat-label {{
            font-size: 0.75rem;
            color: var(--text-secondary);
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.5rem;
        }}

        .stat-value {{
            font-size: 1.75rem;
            font-weight: 700;
            color: var(--text-primary);
            margin-bottom: 0.25rem;
        }}

        .stat-desc {{
            font-size: 0.875rem;
            color: var(--text-secondary);
        }}

        .category-list {{
            margin-top: 1.5rem;
        }}

        .category-item {{
            background: var(--dark-bg);
            border-radius: 6px;
            padding: 0.75rem;
            margin-bottom: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border: 1px solid var(--border-color);
        }}

        .category-name {{
            font-size: 0.875rem;
            color: var(--text-primary);
            font-weight: 500;
        }}

        .category-count {{
            font-size: 0.75rem;
            background: var(--primary-color);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-weight: 600;
        }}

        .node-info {{
            background: var(--dark-bg);
            border-radius: 8px;
            padding: 1rem;
            margin-top: 1rem;
            border: 1px solid var(--border-color);
        }}

        .node-info h3 {{
            font-size: 1rem;
            margin-bottom: 0.75rem;
            color: var(--primary-color);
        }}

        .info-row {{
            display: flex;
            justify-content: space-between;
            padding: 0.5rem 0;
            border-bottom: 1px solid var(--border-color);
            font-size: 0.875rem;
        }}

        .info-row:last-child {{
            border-bottom: none;
        }}

        .info-label {{
            color: var(--text-secondary);
        }}

        .info-value {{
            color: var(--text-primary);
            font-weight: 500;
        }}

        /* Scrollbar Styles */
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}

        ::-webkit-scrollbar-track {{
            background: var(--dark-bg);
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb {{
            background: var(--border-color);
            border-radius: 4px;
        }}

        ::-webkit-scrollbar-thumb:hover {{
            background: var(--primary-color);
        }}

        /* Responsive Design */
        @media (max-width: 1400px) {{
            .dashboard-container {{
                grid-template-columns: 280px 1fr 300px;
            }}
        }}

        @media (max-width: 1024px) {{
            .dashboard-container {{
                grid-template-columns: 1fr;
                grid-template-rows: auto 1fr auto;
            }}

            .sidebar,
            .stats-panel {{
                max-height: 300px;
            }}
        }}
    </style>
</head>
<body>
    <!-- Header -->
    <header class="header">
        <div class="header-content">
            <div class="logo-section">
                <div class="logo">
                    <i class="fas fa-network-wired"></i>
                </div>
                <div class="title-section">
                    <h1>Global Trade Shocks - Sectoral Network Analysis</h1>
                    <p class="subtitle">Interactive 3D Visualization of Indian Economic Sectors</p>
                </div>
            </div>
            <div class="header-actions">
                <button class="btn btn-secondary" onclick="resetView()">
                    <i class="fas fa-redo"></i>
                    Reset View
                </button>
                <button class="btn btn-primary" onclick="exportData()">
                    <i class="fas fa-download"></i>
                    Export Data
                </button>
            </div>
        </div>
    </header>

    <!-- Main Dashboard -->
    <div class="dashboard-container">
        <!-- Left Sidebar - Information & Controls -->
        <aside class="sidebar">
            <h2><i class="fas fa-info-circle"></i> About This Network</h2>

            <div class="info-box">
                <h3>Dataset</h3>
                <p>Indian economic sectors and their trade linkages for analyzing global trade shocks and supply chain vulnerabilities.</p>
            </div>

            <div class="info-box">
                <h3>Network Structure</h3>
                <p>Nodes represent economic sectors. Edges represent input-output relationships and trade flows between sectors.</p>
            </div>

            <div class="control-group">
                <label for="categoryFilter">Filter by Category</label>
                <select id="categoryFilter" onchange="filterByCategory()">
                    <option value="all">All Sectors</option>
                    <option value="Agriculture">Agriculture</option>
                    <option value="Livestock & Food">Livestock & Food</option>
                    <option value="Textiles & Apparel">Textiles & Apparel</option>
                    <option value="Chemicals">Chemicals</option>
                    <option value="Mining & Energy">Mining & Energy</option>
                    <option value="Metals & Manufacturing">Metals & Manufacturing</option>
                    <option value="Machinery & Equipment">Machinery & Equipment</option>
                    <option value="Transport Equipment">Transport Equipment</option>
                    <option value="Services">Services</option>
                    <option value="Infrastructure & Utilities">Infrastructure & Utilities</option>
                    <option value="Other Industries">Other Industries</option>
                </select>
            </div>

            <div class="control-group">
                <label for="searchSector">Search Sector</label>
                <input type="text" id="searchSector" placeholder="Type sector name..." oninput="searchSector(this.value)">
            </div>

            <div class="info-box">
                <h3>Instructions</h3>
                <p><strong>Click</strong> on sectors to view details<br>
                <strong>Drag</strong> to rotate the network<br>
                <strong>Scroll</strong> to zoom in/out</p>
            </div>
        </aside>

        <!-- Main Content Area -->
        <main class="main-content">
            <div class="content-header">
                <h2><i class="fas fa-project-diagram"></i> Sectoral Network Visualization</h2>
                <div class="view-controls">
                    <button class="view-btn active" onclick="setView('3d')" title="3D View">
                        <i class="fas fa-cube"></i>
                    </button>
                    <button class="view-btn" onclick="setView('top')" title="Top View">
                        <i class="fas fa-arrows-alt-v"></i>
                    </button>
                    <button class="view-btn" onclick="setView('side')" title="Side View">
                        <i class="fas fa-arrows-alt-h"></i>
                    </button>
                </div>
            </div>
            <div id="networkPlot"></div>
        </main>

        <!-- Right Sidebar - Statistics -->
        <aside class="stats-panel">
            <h2><i class="fas fa-chart-bar"></i> Network Statistics</h2>

            <div class="stat-card">
                <div class="stat-label">Total Sectors</div>
                <div class="stat-value">{len(node_names)}</div>
                <div class="stat-desc">Economic sectors in network</div>
            </div>

            <div class="stat-card">
                <div class="stat-label">Total Linkages</div>
                <div class="stat-value" id="totalEdges">-</div>
                <div class="stat-desc">Inter-sector connections</div>
            </div>

            <div class="stat-card">
                <div class="stat-label">Network Density</div>
                <div class="stat-value" id="networkDensity">-</div>
                <div class="stat-desc">Connection intensity</div>
            </div>

            <h3 style="margin: 1.5rem 0 1rem; font-size: 1rem; color: var(--text-secondary);">
                <i class="fas fa-layer-group"></i> Sector Categories
            </h3>

            <div class="category-list">
"""

    # Add category counts
    for category, count in sorted(category_counts.items(), key=lambda x: -x[1]):
        if count > 0:
            html_content += f"""                <div class="category-item">
                    <span class="category-name">{category}</span>
                    <span class="category-count">{count}</span>
                </div>
"""

    html_content += f"""            </div>

            <div class="node-info" id="selectedNodeInfo" style="display: none;">
                <h3><i class="fas fa-info-circle"></i> Selected Sector</h3>
                <div class="info-row">
                    <span class="info-label">Name:</span>
                    <span class="info-value" id="sectorName">-</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Category:</span>
                    <span class="info-value" id="sectorCategory">-</span>
                </div>
                <div class="info-row">
                    <span class="info-label">Connections:</span>
                    <span class="info-value" id="sectorDegree">-</span>
                </div>
            </div>
        </aside>
    </div>

    <script>
        // Real network data from your analysis
        const plotlyData = {json.dumps([edge_trace, node_trace])};

        // Sector categorization
        const sectorCategories = {json.dumps(sector_categories)};

        // Category color mapping
        const categoryColors = {json.dumps(category_colors)};

        // Extract network structure
        let networkData = {{
            nodes: [],
            edges: []
        }};

        const edgeTrace = plotlyData[0];
        const nodeTrace = plotlyData[1];

        // Process nodes
        for (let i = 0; i < nodeTrace.x.length; i++) {{
            const sectorName = nodeTrace.text[i];
            const category = sectorCategories[sectorName] || 'Other';

            networkData.nodes.push({{
                id: i,
                name: sectorName,
                x: nodeTrace.x[i],
                y: nodeTrace.y[i],
                z: nodeTrace.z[i],
                category: category,
                categoryColor: categoryColors[category] || 11,
                degree: 0
            }});
        }}

        // Process edges
        let sourceIdx = null;
        for (let i = 0; i < edgeTrace.x.length; i++) {{
            if (edgeTrace.x[i] === null) {{
                sourceIdx = null;
                continue;
            }}

            if (sourceIdx === null) {{
                // Find source node
                for (let j = 0; j < networkData.nodes.length; j++) {{
                    if (Math.abs(networkData.nodes[j].x - edgeTrace.x[i]) < 0.0001 &&
                        Math.abs(networkData.nodes[j].y - edgeTrace.y[i]) < 0.0001 &&
                        Math.abs(networkData.nodes[j].z - edgeTrace.z[i]) < 0.0001) {{
                        sourceIdx = j;
                        break;
                    }}
                }}
            }} else {{
                // Find target node
                for (let j = 0; j < networkData.nodes.length; j++) {{
                    if (Math.abs(networkData.nodes[j].x - edgeTrace.x[i]) < 0.0001 &&
                        Math.abs(networkData.nodes[j].y - edgeTrace.y[i]) < 0.0001 &&
                        Math.abs(networkData.nodes[j].z - edgeTrace.z[i]) < 0.0001) {{
                        networkData.edges.push({{
                            source: sourceIdx,
                            target: j
                        }});
                        networkData.nodes[sourceIdx].degree++;
                        networkData.nodes[j].degree++;
                        break;
                    }}
                }}
                sourceIdx = null;
            }}
        }}

        console.log(`Loaded ${{networkData.nodes.length}} sectors and ${{networkData.edges.length}} linkages`);

        // Initialize visualization
        function initializeVisualization() {{
            // Prepare edge coordinates
            const edgeX = [];
            const edgeY = [];
            const edgeZ = [];

            networkData.edges.forEach(edge => {{
                const source = networkData.nodes[edge.source];
                const target = networkData.nodes[edge.target];
                edgeX.push(source.x, target.x, null);
                edgeY.push(source.y, target.y, null);
                edgeZ.push(source.z, target.z, null);
            }});

            const edgeTraceViz = {{
                x: edgeX,
                y: edgeY,
                z: edgeZ,
                mode: 'lines',
                type: 'scatter3d',
                line: {{
                    color: 'rgba(148, 163, 184, 0.2)',
                    width: 1
                }},
                hoverinfo: 'none',
                showlegend: false
            }};

            // Prepare node data
            const nodeX = networkData.nodes.map(n => n.x);
            const nodeY = networkData.nodes.map(n => n.y);
            const nodeZ = networkData.nodes.map(n => n.z);
            const nodeText = networkData.nodes.map(n =>
                `<b>${{n.name}}</b><br>Category: ${{n.category}}<br>Connections: ${{n.degree}}`
            );
            const nodeColors = networkData.nodes.map(n => n.categoryColor);
            const nodeSizes = networkData.nodes.map(n => Math.max(5, n.degree * 0.5 + 5));

            const nodeTraceViz = {{
                x: nodeX,
                y: nodeY,
                z: nodeZ,
                mode: 'markers',
                type: 'scatter3d',
                marker: {{
                    size: nodeSizes,
                    color: nodeColors,
                    colorscale: 'Viridis',
                    showscale: true,
                    line: {{
                        color: '#2563eb',
                        width: 0.5
                    }},
                    colorbar: {{
                        title: 'Category',
                        thickness: 15,
                        len: 0.7,
                        bgcolor: '#1e293b',
                        tickfont: {{ color: '#f1f5f9' }},
                        titlefont: {{ color: '#f1f5f9' }},
                        tickmode: 'array',
                        tickvals: Object.values(categoryColors),
                        ticktext: Object.keys(categoryColors)
                    }}
                }},
                text: networkData.nodes.map(n => n.name),
                hovertext: nodeText,
                hoverinfo: 'text',
                showlegend: false
            }};

            const data = [edgeTraceViz, nodeTraceViz];

            const layout = {{
                title: '',
                showlegend: false,
                hovermode: 'closest',
                margin: {{ l: 0, r: 0, b: 0, t: 0 }},
                paper_bgcolor: '#1e293b',
                plot_bgcolor: '#1e293b',
                scene: {{
                    xaxis: {{
                        showbackground: false,
                        showgrid: false,
                        showline: false,
                        zeroline: false,
                        showticklabels: false,
                        title: ''
                    }},
                    yaxis: {{
                        showbackground: false,
                        showgrid: false,
                        showline: false,
                        zeroline: false,
                        showticklabels: false,
                        title: ''
                    }},
                    zaxis: {{
                        showbackground: false,
                        showgrid: false,
                        showline: false,
                        zeroline: false,
                        showticklabels: false,
                        title: ''
                    }},
                    camera: {{
                        eye: {{ x: 1.5, y: 1.5, z: 1.5 }}
                    }},
                    bgcolor: '#1e293b'
                }}
            }};

            const config = {{
                responsive: true,
                displayModeBar: true,
                displaylogo: false,
                modeBarButtonsToRemove: ['toImage'],
                modeBarButtonsToAdd: [{{
                    name: 'Capture',
                    icon: Plotly.Icons.camera,
                    click: function(gd) {{
                        Plotly.downloadImage(gd, {{
                            format: 'png',
                            width: 1920,
                            height: 1080,
                            filename: 'trade_network_sectoral_analysis'
                        }});
                    }}
                }}]
            }};

            Plotly.newPlot('networkPlot', data, layout, config);

            // Add click event
            document.getElementById('networkPlot').on('plotly_click', function(data) {{
                const nodeIndex = data.points[0].pointIndex;
                const node = networkData.nodes[nodeIndex];
                showSectorInfo(node);
            }});

            // Update statistics
            updateStatistics();
        }}

        function updateStatistics() {{
            document.getElementById('totalEdges').textContent = networkData.edges.length;

            const maxPossibleEdges = networkData.nodes.length * (networkData.nodes.length - 1) / 2;
            const density = (networkData.edges.length / maxPossibleEdges).toFixed(3);
            document.getElementById('networkDensity').textContent = density;
        }}

        function showSectorInfo(node) {{
            document.getElementById('selectedNodeInfo').style.display = 'block';
            document.getElementById('sectorName').textContent = node.name;
            document.getElementById('sectorCategory').textContent = node.category;
            document.getElementById('sectorDegree').textContent = node.degree;
        }}

        function filterByCategory() {{
            const selected = document.getElementById('categoryFilter').value;
            console.log('Filter by category:', selected);
            // TODO: Implement filtering logic
        }}

        function searchSector(query) {{
            if (!query) return;
            query = query.toLowerCase();
            const matches = networkData.nodes.filter(n =>
                n.name.toLowerCase().includes(query)
            );
            console.log('Search results:', matches);
        }}

        function setView(view) {{
            const buttons = document.querySelectorAll('.view-btn');
            buttons.forEach(btn => btn.classList.remove('active'));
            event.target.closest('.view-btn').classList.add('active');

            const cameras = {{
                '3d': {{ x: 1.5, y: 1.5, z: 1.5 }},
                'top': {{ x: 0, y: 0, z: 2.5 }},
                'side': {{ x: 2.5, y: 0, z: 0 }}
            }};

            Plotly.relayout('networkPlot', {{
                'scene.camera.eye': cameras[view]
            }});
        }}

        function resetView() {{
            Plotly.relayout('networkPlot', {{
                'scene.camera.eye': {{ x: 1.5, y: 1.5, z: 1.5 }}
            }});
        }}

        function exportData() {{
            const exportObj = {{
                sectors: networkData.nodes.map(n => ({{
                    name: n.name,
                    category: n.category,
                    connections: n.degree
                }})),
                linkages: networkData.edges.length,
                categories: sectorCategories
            }};

            const dataStr = JSON.stringify(exportObj, null, 2);
            const dataBlob = new Blob([dataStr], {{ type: 'application/json' }});
            const url = URL.createObjectURL(dataBlob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'sectoral_network_data.json';
            link.click();
        }}

        // Initialize on page load
        window.addEventListener('load', () => {{
            initializeVisualization();
        }});

        // Handle window resize
        window.addEventListener('resize', () => {{
            Plotly.Plots.resize('networkPlot');
        }});
    </script>
</body>
</html>
"""

    # Write the file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\nDashboard created successfully!")
    print(f"Sectors: {len(node_names)}")
    print(f"Categories: {len([c for c in category_counts.values() if c > 0])}")
    print(f"Output: {output_file}")

def main():
    script_dir = Path(__file__).parent
    original_file = script_dir / "network_3d_visualization.html"
    output_file = script_dir / "trade_network_dashboard.html"

    # Extract data
    data = extract_network_data(original_file)

    if data:
        # Create annotated dashboard
        create_annotated_dashboard(data, output_file)
        print(f"\nSUCCESS! Open {output_file} in your browser")
    else:
        print("Failed to extract network data")

if __name__ == "__main__":
    main()
