"""
Fix the enhanced dashboard by properly loading network data
"""
import re
import json
from pathlib import Path

def extract_plotly_call(html_file):
    """Extract the complete Plotly.newPlot call"""
    print(f"Reading {html_file}...")

    with open(html_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Plotly.newPlot call - more robust pattern
    # Look for the script tag containing Plotly.newPlot
    pattern = r'Plotly\.newPlot\s*\(\s*["\']([^"\']+)["\']\s*,\s*(\[[\s\S]+?\])\s*,\s*(\{[\s\S]+?\})\s*,\s*(\{[\s\S]+?\})\s*\);'

    match = re.search(pattern, content)

    if match:
        div_id = match.group(1)
        data = match.group(2)
        layout = match.group(3)
        config = match.group(4)

        print(f"[OK] Found Plotly visualization")
        print(f"  Div ID: {div_id}")
        print(f"  Data length: {len(data)} chars")
        print(f"  Layout length: {len(layout)} chars")

        return data, layout, config

    print("[ERROR] Could not find Plotly.newPlot call")

    # Try simpler pattern
    simple_pattern = r'Plotly\.newPlot\([^,]+,\s*(\[[^\]]+\])'
    simple_match = re.search(simple_pattern, content[:50000])  # Check first 50k chars

    if simple_match:
        print("[INFO] Found with simple pattern, trying detailed extraction...")
        # Find the full data section manually
        start_idx = content.find('Plotly.newPlot')
        if start_idx > 0:
            # Extract a large chunk
            chunk = content[start_idx:start_idx + 200000]
            # Count brackets to find matching close
            bracket_count = 0
            data_start = chunk.find('[')
            if data_start > 0:
                data_content = '['
                in_string = False
                escape = False
                for i, char in enumerate(chunk[data_start+1:], 1):
                    data_content += char
                    if escape:
                        escape = False
                        continue
                    if char == '\\':
                        escape = True
                    elif char == '"':
                        in_string = not in_string
                    elif not in_string:
                        if char == '[':
                            bracket_count += 1
                        elif char == ']':
                            if bracket_count == 0:
                                print(f"[OK] Extracted data: {len(data_content)} chars")
                                return data_content, '{}', '{}'
                            bracket_count -= 1

    return None, None, None

def create_fixed_dashboard(original_file, template_file, output_file):
    """Create a working dashboard with the actual data"""

    # Extract data from original
    data, layout, config = extract_plotly_call(original_file)

    if not data:
        print("Failed to extract data!")
        return

    # Read template
    print(f"\nReading template {template_file}...")
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()

    # Create the JavaScript to inject
    js_injection = f"""
    <script>
        // Actual network data from original visualization
        const originalPlotlyData = {data};
        const originalPlotlyLayout = {layout};

        // Parse data into our format
        networkData = {{
            nodes: [],
            edges: []
        }};

        console.log('Loading network data...');
        console.log('Plotly data traces:', originalPlotlyData.length);

        if (originalPlotlyData && originalPlotlyData.length >= 2) {{
            const edgeTrace = originalPlotlyData[0];
            const nodeTrace = originalPlotlyData[1];

            console.log('Edge trace points:', edgeTrace.x ? edgeTrace.x.length : 0);
            console.log('Node trace points:', nodeTrace.x ? nodeTrace.x.length : 0);

            // Extract nodes from node trace
            if (nodeTrace.x && nodeTrace.y && nodeTrace.z) {{
                for (let i = 0; i < nodeTrace.x.length; i++) {{
                    const nodeName = nodeTrace.text && nodeTrace.text[i] ?
                        nodeTrace.text[i] : `Node ${{i}}`;

                    let size = 8;
                    if (nodeTrace.marker && nodeTrace.marker.size) {{
                        size = Array.isArray(nodeTrace.marker.size) ?
                            nodeTrace.marker.size[i] : nodeTrace.marker.size;
                    }}

                    let community = 0;
                    if (nodeTrace.marker && nodeTrace.marker.color) {{
                        community = Array.isArray(nodeTrace.marker.color) ?
                            nodeTrace.marker.color[i] : 0;
                    }}

                    networkData.nodes.push({{
                        id: i,
                        name: nodeName,
                        x: nodeTrace.x[i],
                        y: nodeTrace.y[i],
                        z: nodeTrace.z[i],
                        size: size,
                        degree: 0,
                        centrality: Math.random(),
                        community: community
                    }});
                }}
            }}

            // Extract edges from edge trace
            // Edge trace has format: [x1, x2, null, x3, x4, null, ...]
            if (edgeTrace.x && edgeTrace.y && edgeTrace.z) {{
                let sourceIdx = null;
                let sourceX = null, sourceY = null, sourceZ = null;

                for (let i = 0; i < edgeTrace.x.length; i++) {{
                    if (edgeTrace.x[i] === null ||
                        edgeTrace.y[i] === null ||
                        edgeTrace.z[i] === null) {{
                        sourceIdx = null;
                        continue;
                    }}

                    if (sourceIdx === null) {{
                        // This is a source node
                        sourceX = edgeTrace.x[i];
                        sourceY = edgeTrace.y[i];
                        sourceZ = edgeTrace.z[i];

                        // Find which node this is
                        for (let j = 0; j < networkData.nodes.length; j++) {{
                            if (Math.abs(networkData.nodes[j].x - sourceX) < 0.001 &&
                                Math.abs(networkData.nodes[j].y - sourceY) < 0.001 &&
                                Math.abs(networkData.nodes[j].z - sourceZ) < 0.001) {{
                                sourceIdx = j;
                                break;
                            }}
                        }}
                    }} else {{
                        // This is a target node
                        const targetX = edgeTrace.x[i];
                        const targetY = edgeTrace.y[i];
                        const targetZ = edgeTrace.z[i];

                        // Find which node this is
                        for (let j = 0; j < networkData.nodes.length; j++) {{
                            if (Math.abs(networkData.nodes[j].x - targetX) < 0.001 &&
                                Math.abs(networkData.nodes[j].y - targetY) < 0.001 &&
                                Math.abs(networkData.nodes[j].z - targetZ) < 0.001) {{
                                networkData.edges.push({{
                                    source: sourceIdx,
                                    target: j,
                                    weight: 1
                                }});
                                networkData.nodes[sourceIdx].degree++;
                                networkData.nodes[j].degree++;
                                break;
                            }}
                        }}
                        sourceIdx = null;
                    }}
                }}
            }}
        }}

        console.log(`Loaded ${{networkData.nodes.length}} nodes and ${{networkData.edges.length}} edges`);

        // Override the sample data generation
        function generateSampleData() {{
            // Do nothing - we have real data
            console.log('Using real network data instead of sample');
        }}
    </script>
    """

    # Find where to inject (before the existing script that generates sample data)
    # Look for the script tag that contains generateSampleData
    pattern = r'(<script>\s*// Sample network data)'

    if re.search(pattern, template):
        # Inject before the sample data script
        modified = re.sub(pattern, js_injection + r'\n\1', template)
    else:
        # Fallback: inject before closing body tag
        modified = template.replace('</body>', js_injection + '\n</body>')

    # Write the fixed dashboard
    print(f"\nWriting fixed dashboard to {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(modified)

    print("Done! Dashboard created successfully.")
    print(f"\nOpen {output_file} in your browser to view the enhanced dashboard.")

def main():
    script_dir = Path(__file__).parent

    original_file = script_dir / "network_3d_visualization.html"
    template_file = script_dir / "network_3d_visualization_enhanced.html"
    output_file = script_dir / "network_3d_dashboard_final.html"

    if not original_file.exists():
        print(f"Error: Original file not found: {original_file}")
        return

    if not template_file.exists():
        print(f"Error: Template file not found: {template_file}")
        return

    create_fixed_dashboard(original_file, template_file, output_file)

if __name__ == "__main__":
    main()
