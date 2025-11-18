"""
Script to extract network data from original Plotly HTML and inject into enhanced dashboard
"""

import re
import json
from pathlib import Path

def extract_plotly_data(html_file):
    """Extract Plotly data from HTML file"""
    print(f"Reading {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Plotly.newPlot call
    pattern = r'Plotly\.newPlot\s*\(\s*["\']([^"\']+)["\']\s*,\s*(\[[\s\S]*?\])\s*,'
    match = re.search(pattern, content)

    if not match:
        print("Could not find Plotly data in the file")
        return None

    div_id = match.group(1)
    data_str = match.group(2)

    print(f"Found Plotly div ID: {div_id}")
    print(f"Extracted data (first 200 chars): {data_str[:200]}...")

    return data_str

def create_enhanced_html_with_data(data_str, output_file, template_file):
    """Create enhanced HTML with actual network data"""
    print(f"Reading template {template_file}...")

    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()

    # Create the replacement script with actual data
    replacement_script = f"""
    <script>
        // Load actual network data from original visualization
        let plotlyData = {data_str};

        // Extract nodes and edges from Plotly data
        networkData = {{
            nodes: [],
            edges: []
        }};

        // Parse the Plotly data structure
        if (plotlyData && plotlyData.length >= 2) {{
            const edgeTrace = plotlyData[0];
            const nodeTrace = plotlyData[1];

            // Extract nodes
            if (nodeTrace.x && nodeTrace.y && nodeTrace.z) {{
                for (let i = 0; i < nodeTrace.x.length; i++) {{
                    const nodeName = nodeTrace.text && nodeTrace.text[i] ? nodeTrace.text[i] : `Node ${{i}}`;
                    const size = nodeTrace.marker && nodeTrace.marker.size ?
                        (Array.isArray(nodeTrace.marker.size) ? nodeTrace.marker.size[i] : nodeTrace.marker.size) : 8;
                    const color = nodeTrace.marker && nodeTrace.marker.color ?
                        (Array.isArray(nodeTrace.marker.color) ? nodeTrace.marker.color[i] : 0) : 0;

                    networkData.nodes.push({{
                        id: i,
                        name: nodeName,
                        x: nodeTrace.x[i],
                        y: nodeTrace.y[i],
                        z: nodeTrace.z[i],
                        size: size,
                        degree: 0,
                        centrality: Math.random(), // Calculate from network if available
                        community: color
                    }});
                }}
            }}

            // Extract edges from edge trace
            if (edgeTrace.x && edgeTrace.y && edgeTrace.z) {{
                let sourceIdx = null;
                for (let i = 0; i < edgeTrace.x.length; i++) {{
                    if (edgeTrace.x[i] === null) {{
                        sourceIdx = null;
                        continue;
                    }}

                    if (sourceIdx === null) {{
                        // Find which node this coordinate belongs to
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
                                    target: j,
                                    weight: 1
                                }});
                                networkData.nodes[sourceIdx].degree++;
                                networkData.nodes[j].degree++;
                                sourceIdx = null;
                                break;
                            }}
                        }}
                    }}
                }}
            }}
        }}

        console.log(`Loaded ${{networkData.nodes.length}} nodes and ${{networkData.edges.length}} edges`);

        // Initialize visualization with actual data
        function initializeVisualization() {{
            if (networkData.nodes.length === 0) {{
                console.warn("No network data available, using sample data");
                generateSampleData();
            }}

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

            const edgeTrace = {{
                x: edgeX,
                y: edgeY,
                z: edgeZ,
                mode: 'lines',
                type: 'scatter3d',
                line: {{
                    color: 'rgba(148, 163, 184, 0.3)',
                    width: 0.5
                }},
                hoverinfo: 'none',
                showlegend: false
            }};

            const nodeX = networkData.nodes.map(n => n.x);
            const nodeY = networkData.nodes.map(n => n.y);
            const nodeZ = networkData.nodes.map(n => n.z);
            const nodeText = networkData.nodes.map(n =>
                `${{n.name}}<br>Degree: ${{n.degree}}<br>Centrality: ${{n.centrality.toFixed(2)}}`
            );
            const nodeColors = networkData.nodes.map(n => n.community);

            const nodeTrace = {{
                x: nodeX,
                y: nodeY,
                z: nodeZ,
                mode: 'markers+text',
                type: 'scatter3d',
                text: networkData.nodes.map(n => n.name),
                textposition: 'top center',
                textfont: {{
                    size: 8,
                    color: '#f1f5f9'
                }},
                marker: {{
                    size: networkData.nodes.map(n => n.size),
                    color: nodeColors,
                    colorscale: 'Viridis',
                    showscale: true,
                    line: {{
                        color: '#2563eb',
                        width: 0.5
                    }},
                    colorbar: {{
                        title: 'Community',
                        thickness: 15,
                        len: 0.7,
                        bgcolor: '#1e293b',
                        tickfont: {{ color: '#f1f5f9' }},
                        titlefont: {{ color: '#f1f5f9' }}
                    }}
                }},
                hovertext: nodeText,
                hoverinfo: 'text',
                showlegend: false
            }};

            const data = [edgeTrace, nodeTrace];

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
                            filename: 'network_visualization'
                        }});
                    }}
                }}]
            }};

            Plotly.newPlot('networkPlot', data, layout, config);

            // Add click event listener
            document.getElementById('networkPlot').on('plotly_click', function(data) {{
                const nodeIndex = data.points[0].pointIndex;
                const node = networkData.nodes[nodeIndex];
                showNodeInfo(node);
            }});

            // Update statistics
            updateStatistics();
        }}

        // Initialize on page load
        window.addEventListener('load', () => {{
            initializeVisualization();
        }});
    </script>
    """

    # Find and replace the existing script section that initializes visualization
    # Look for the script tag before </body>
    script_pattern = r'(<script>[\s\S]*?// Generate sample data for demonstration[\s\S]*?</script>\s*</body>)'

    if re.search(script_pattern, template):
        enhanced_html = re.sub(script_pattern, replacement_script + '\n</body>', template)
    else:
        # If pattern not found, append before </body>
        enhanced_html = template.replace('</body>', replacement_script + '\n</body>')

    print(f"Writing enhanced dashboard to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(enhanced_html)

    print("✓ Enhanced dashboard created successfully!")

def main():
    # File paths
    script_dir = Path(__file__).parent
    original_file = script_dir / "network_3d_visualization.html"
    template_file = script_dir / "network_3d_visualization_enhanced.html"
    output_file = script_dir / "network_3d_dashboard_final.html"

    # Extract data from original file
    data_str = extract_plotly_data(original_file)

    if data_str:
        # Create enhanced HTML with actual data
        create_enhanced_html_with_data(data_str, output_file, template_file)
        print(f"\n✓ Final dashboard saved to: {output_file}")
        print("\nOpen the file in your browser to view the enhanced dashboard!")
    else:
        print("Failed to extract data from original file")

if __name__ == "__main__":
    main()
