"""
Input-Output Table Processing Script
Calculates technical coefficients, Leontief inverse, linkages, and network metrics
Based on iotable_processing.ipynb notebook implementation
"""

import pandas as pd
import numpy as np
import networkx as nx
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Configuration
DATA_DIR = Path("./data")
PROCESSED_DIR = DATA_DIR / "processed"
IO_DIR = DATA_DIR / "processed_io_data"

# Ensure directories exist
IO_DIR.mkdir(parents=True, exist_ok=True)


def load_io_matrix() -> tuple:
    """Load and extract use matrix from MOSPI data"""
    print("Loading I-O matrix...")

    io_df = pd.read_csv(PROCESSED_DIR / "MOSPI Matrix Final - ALL.csv", header=1)

    # Get sector names (rows 0-130, column 1)
    sector_names = io_df.iloc[0:131, 1].copy()

    # Get use matrix (rows 0-130, columns 2:133)
    use_matrix = io_df.iloc[0:131, 2:133].copy()

    # Get Total Output (row 134, columns 2:133)
    total_output = io_df.iloc[134, 2:133].copy()

    print(f"✓ Use matrix shape: {use_matrix.shape}")
    print(f"✓ Total output length: {len(total_output)}")
    print(f"✓ Sector names: {len(sector_names)}")

    return sector_names, use_matrix, total_output


def calculate_technical_coefficients(use_matrix: pd.DataFrame,
                                     total_output: pd.Series,
                                     sector_names: pd.Series) -> pd.DataFrame:
    """
    Calculate technical coefficients matrix
    a_ij = input_ij / totaloutput_j
    """
    print("\nCalculating technical coefficients...")

    # Calculate coefficients
    tech_coef = use_matrix.div(total_output, axis=1)
    tech_coef = tech_coef.fillna(0)

    # Add sector names
    tech_coef.insert(0, 'sector_name', sector_names.values)

    # Check stats
    print(f"✓ Technical coefficient stats:")
    print(f"  Negative values: {(tech_coef.iloc[:, 1:] < 0).sum().sum()}")
    print(f"  Values > 1: {(tech_coef.iloc[:, 1:] > 1).sum().sum()}")

    # Save
    output_path = IO_DIR / "technical_coefficients.csv"
    tech_coef.to_csv(output_path, index=False)
    print(f"✓ Saved: {output_path}")

    return tech_coef


def calculate_leontief_inverse(tech_coef: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate Leontief Inverse matrix
    L = (I - A)^-1
    """
    print("\nCalculating Leontief inverse...")

    # Get the coefficients matrix (exclude sector name)
    sector_names = tech_coef['sector_name']
    A = tech_coef.drop(columns=["sector_name"]).values

    n = A.shape[0]
    print(f"✓ Matrix size: {n} x {n}")

    # Create identity matrix
    I = np.eye(n)

    # Calculate Leontief inverse
    try:
        leontief_inverse = np.linalg.inv(I - A)
        print("✓ Leontief inverse calculated successfully")
    except np.linalg.LinAlgError:
        print("! Using pseudo-inverse (matrix is singular)")
        leontief_inverse = np.linalg.pinv(I - A)

    # Convert to dataframe
    leontief_df = pd.DataFrame(
        leontief_inverse,
        index=sector_names,
        columns=sector_names
    )

    # Save
    output_path = IO_DIR / "leontief_inverse.csv"
    leontief_df.to_csv(output_path)
    print(f"✓ Saved: {output_path}")

    return leontief_df


def calculate_linkages(leontief_df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate backward and forward linkages
    Backward Linkage = Sum of Column
    Forward Linkage = Sum of Row
    """
    print("\nCalculating backward and forward linkages...")

    # Calculate linkages
    backward_linkage = leontief_df.sum(axis=0)
    forward_linkage = leontief_df.sum(axis=1)

    # Identify key sectors
    avg_backward = backward_linkage.mean()
    avg_forward = forward_linkage.mean()

    print(f"✓ Average backward linkage: {avg_backward:.2f}")
    print(f"✓ Average forward linkage: {avg_forward:.2f}")

    # Create nodes dataframe
    nodes_df = pd.DataFrame({
        'sector_name': leontief_df.index,
        'backward_linkage': backward_linkage.values,
        'forward_linkage': forward_linkage.values,
        'is_key_sector': (backward_linkage.values > avg_backward) &
                        (forward_linkage.values > avg_forward)
    })

    # Add sector_id
    nodes_df.insert(0, 'sector_id', range(1, len(nodes_df) + 1))

    # Save
    output_path = IO_DIR / "production_network_nodes.csv"
    nodes_df.to_csv(output_path, index=False)
    print(f"✓ Saved: {output_path}")

    print(f"\n✓ Total sectors: {len(nodes_df)}")
    print(f"✓ Key sectors: {nodes_df['is_key_sector'].sum()}")

    return nodes_df


def create_network_edges(tech_coef: pd.DataFrame,
                        use_matrix: pd.DataFrame,
                        threshold: float = 0.001) -> pd.DataFrame:
    """Create network edge list from technical coefficients"""
    print("\nCreating network edge list...")

    # Get sector names
    sector_names = tech_coef['sector_name']

    # Rename tech_coef columns to match sector names
    tech_coef_fixed = tech_coef.copy()
    tech_coef_fixed.columns = ['sector_name'] + sector_names.tolist()

    # Prepare use_matrix
    use_matrix_reload = use_matrix.apply(pd.to_numeric, errors='coerce').fillna(0)

    # Build edges
    edges = []
    for i in range(len(tech_coef_fixed)):
        source_sector = tech_coef_fixed.iloc[i]['sector_name']

        for j, target_sector in enumerate(sector_names):
            coefficient = tech_coef_fixed.iloc[i, j + 1]

            if coefficient > threshold:
                edges.append({
                    'source_sector': source_sector,
                    'target_sector': target_sector,
                    'input_coefficient': coefficient,
                    'input_value': use_matrix_reload.iloc[i, j]
                })

    edges_df = pd.DataFrame(edges)

    # Save
    output_path = IO_DIR / "production_network_edges.csv"
    edges_df.to_csv(output_path, index=False)
    print(f"✓ Saved: {output_path}")
    print(f"✓ Created {len(edges_df):,} network edges")

    return edges_df


def calculate_network_metrics(edges_df: pd.DataFrame,
                              nodes_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate network centrality metrics"""
    print("\nCalculating network centrality metrics...")

    # Create directed graph
    G = nx.from_pandas_edgelist(
        edges_df,
        source='source_sector',
        target='target_sector',
        edge_attr='input_coefficient',
        create_using=nx.DiGraph()
    )

    print(f"✓ Network created:")
    print(f"  Nodes: {G.number_of_nodes()}")
    print(f"  Edges: {G.number_of_edges()}")
    print(f"  Density: {nx.density(G):.4f}")

    # Calculate centrality measures
    print("\n  Calculating centrality metrics...")
    degree_centrality = nx.degree_centrality(G)
    betweenness = nx.betweenness_centrality(G)
    closeness = nx.closeness_centrality(G)
    eigenvector = nx.eigenvector_centrality(G, max_iter=1000)
    pagerank = nx.pagerank(G)
    print("  ✓ All centrality metrics calculated")

    # Combine with nodes dataframe
    network_metrics = nodes_df.copy()
    network_metrics['degree_centrality'] = network_metrics['sector_name'].map(degree_centrality)
    network_metrics['betweenness_centrality'] = network_metrics['sector_name'].map(betweenness)
    network_metrics['closeness_centrality'] = network_metrics['sector_name'].map(closeness)
    network_metrics['eigenvector_centrality'] = network_metrics['sector_name'].map(eigenvector)
    network_metrics['pagerank'] = network_metrics['sector_name'].map(pagerank)

    # Fill NaN with 0
    network_metrics = network_metrics.fillna(0)

    # Save
    output_path = IO_DIR / "network_metrics.csv"
    network_metrics.to_csv(output_path, index=False)
    print(f"✓ Saved: {output_path}")

    return network_metrics


def print_summary(network_metrics: pd.DataFrame):
    """Print summary of results"""
    print("\n" + "="*70)
    print("INPUT-OUTPUT TABLE PROCESSING COMPLETE!")
    print("="*70)

    print("\nKEY FINDINGS:")
    print(f"  • {len(network_metrics)} sectors analyzed")
    print(f"  • {network_metrics['is_key_sector'].sum()} key sectors identified")

    print("\nTOP 5 SECTORS BY PAGERANK:")
    top_pagerank = network_metrics.nlargest(5, 'pagerank')[
        ['sector_name', 'pagerank', 'backward_linkage', 'forward_linkage']
    ]
    for _, row in top_pagerank.iterrows():
        print(f"  • {row['sector_name'][:40]:40} PageRank: {row['pagerank']:.6f}")

    print("\nTOP 5 BRIDGE SECTORS (Betweenness):")
    top_betweenness = network_metrics.nlargest(5, 'betweenness_centrality')[
        ['sector_name', 'betweenness_centrality']
    ]
    for _, row in top_betweenness.iterrows():
        print(f"  • {row['sector_name'][:40]:40} Betweenness: {row['betweenness_centrality']:.6f}")

    print("\nTOP KEY SECTORS (High Linkages):")
    key_sectors = network_metrics[network_metrics['is_key_sector']].nlargest(
        5, 'pagerank'
    )[['sector_name', 'backward_linkage', 'forward_linkage']]
    for _, row in key_sectors.iterrows():
        print(f"  • {row['sector_name'][:40]:40} B/F: {row['backward_linkage']:.2f}/{row['forward_linkage']:.2f}")


def main():
    """Run complete I-O table processing pipeline"""
    print("="*70)
    print("INPUT-OUTPUT TABLE PROCESSING PIPELINE")
    print("="*70)

    # Step 1: Load I-O matrix
    sector_names, use_matrix, total_output = load_io_matrix()

    # Step 2: Calculate technical coefficients
    tech_coef = calculate_technical_coefficients(use_matrix, total_output, sector_names)

    # Step 3: Calculate Leontief inverse
    leontief_df = calculate_leontief_inverse(tech_coef)

    # Step 4: Calculate linkages
    nodes_df = calculate_linkages(leontief_df)

    # Step 5: Create network edges
    edges_df = create_network_edges(tech_coef, use_matrix)

    # Step 6: Calculate network metrics
    network_metrics = calculate_network_metrics(edges_df, nodes_df)

    # Step 7: Print summary
    print_summary(network_metrics)

    print("\n" + "="*70)
    print(f"All files saved to: {IO_DIR}")
    print("="*70)


if __name__ == "__main__":
    main()
