"""
Create an annotated dashboard with real sector data
Simple extraction from known position
"""

import json
import re
from pathlib import Path

# Read the HTML file
html_file = Path(__file__).parent / "network_3d_visualization.html"
print(f"Reading {html_file}...")

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the plotly div
div_pos = content.find('class="plotly-graph-div"')
plot_call_pos = content.find('Plotly.newPlot', div_pos)

print(f"Found Plotly.newPlot at position {plot_call_pos}")

# Extract just the data array portion
# Start after the div ID
data_start = content.find('[{', plot_call_pos)
print(f"Data starts at position {data_start}")

# Now we need to find the end of this data array
# It ends with }] before the next parameter (layout object)
# Look for pattern: }],\s*{
end_pattern = r'\}\]\s*,\s*\{'
match = re.search(end_pattern, content[data_start:data_start+2000000])

if match:
    data_end = data_start + match.start() + 2  # Include the }]
    data_json_str = content[data_start:data_end]

    print(f"Extracted {len(data_json_str)} characters")
    print(f"First 200 chars: {data_json_str[:200]}")
    print(f"Last 200 chars: {data_json_str[-200:]}")

    # Parse the JSON
    try:
        data = json.loads(data_json_str)
        print(f"\nSuccessfully parsed! Found {len(data)} traces")

        # Get sector names
        if len(data) >= 2:
            node_trace = data[1]
            sector_names = node_trace.get('text', [])
            print(f"Found {len(sector_names)} sectors")
            print(f"\nFirst 10 sectors:")
            for i, name in enumerate(sector_names[:10]):
                print(f"  {i+1}. {name}")

            # Save the extracted data
            output_data = {
                'edge_trace': data[0],
                'node_trace': data[1],
                'sector_count': len(sector_names),
                'sectors': sector_names
            }

            with open('extracted_network_data.json', 'w', encoding='utf-8') as f:
                json.dump(output_data, f, indent=2)

            print(f"\nData saved to extracted_network_data.json")
            print("Now creating the annotated dashboard...")

            # Import and run the dashboard creation
            import sys
            sys.path.insert(0, str(Path(__file__).parent))

            from extract_real_data import create_annotated_dashboard, categorize_sectors

            output_file = Path(__file__).parent / "trade_network_dashboard.html"
            create_annotated_dashboard(data, output_file)

    except json.JSONDecodeError as e:
        print(f"JSON parse error: {e}")
        print(f"Error at position: {e.pos}")
        if e.pos:
            print(f"Context: {data_json_str[max(0, e.pos-50):e.pos+50]}")
else:
    print("Could not find end of data array")
