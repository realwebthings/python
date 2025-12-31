# 🕸️ Graph Theory for ML/AI

## 📋 Table of Contents
- [Overview](#overview)
- [Graph Fundamentals](#graph-fundamentals)
- [Graph Representations](#graph-representations)
- [Graph Algorithms](#graph-algorithms)
- [Spectral Graph Theory](#spectral-graph-theory)
- [Random Graphs](#random-graphs)
- [Graph Neural Networks](#graph-neural-networks)
- [Applications in ML/AI](#applications-in-mlai)
- [Practice Problems](#practice-problems)
- [Python Implementation](#python-implementation)

---

## Overview

Graph theory is the **mathematics of networks and relationships**, fundamental to modern ML/AI:

### 🎯 **Critical Applications:**
- **Graph Neural Networks**: Learning on graph-structured data
- **Social Network Analysis**: Understanding connections and influence
- **Knowledge Graphs**: Representing structured knowledge
- **Recommendation Systems**: User-item interaction graphs
- **Computer Vision**: Scene graphs and object relationships
- **Natural Language Processing**: Dependency parsing and semantic graphs
- **Reinforcement Learning**: State-action graphs and planning

---

## Graph Fundamentals

### Basic Definitions

#### **Graph**
G = (V, E) where V is a set of vertices (nodes) and E is a set of edges.

#### **Types of Graphs**
- **Undirected**: Edges have no direction
- **Directed (Digraph)**: Edges have direction
- **Weighted**: Edges have weights/costs
- **Simple**: No self-loops or multiple edges
- **Complete**: Every pair of vertices is connected

```python
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from collections import defaultdict, deque

def create_example_graphs():
    """Create and visualize different types of graphs"""
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    # 1. Simple undirected graph
    G1 = nx.Graph()
    G1.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
    pos1 = nx.spring_layout(G1)
    nx.draw(G1, pos1, ax=axes[0, 0], with_labels=True, node_color='lightblue', 
            node_size=500, font_size=16, font_weight='bold')
    axes[0, 0].set_title('Simple Undirected Graph')
    
    # 2. Directed graph
    G2 = nx.DiGraph()
    G2.add_edges_from([(1, 2), (2, 3), (3, 1), (2, 4), (4, 3)])
    pos2 = nx.spring_layout(G2)
    nx.draw(G2, pos2, ax=axes[0, 1], with_labels=True, node_color='lightcoral', 
            node_size=500, font_size=16, font_weight='bold', arrows=True)
    axes[0, 1].set_title('Directed Graph')
    
    # 3. Weighted graph
    G3 = nx.Graph()
    G3.add_weighted_edges_from([(1, 2, 0.5), (2, 3, 1.2), (3, 4, 0.8), (4, 1, 1.0)])
    pos3 = nx.spring_layout(G3)
    nx.draw(G3, pos3, ax=axes[0, 2], with_labels=True, node_color='lightgreen', 
            node_size=500, font_size=16, font_weight='bold')
    edge_labels = nx.get_edge_attributes(G3, 'weight')
    nx.draw_networkx_edge_labels(G3, pos3, edge_labels, ax=axes[0, 2])
    axes[0, 2].set_title('Weighted Graph')
    
    # 4. Complete graph K5
    G4 = nx.complete_graph(5)
    pos4 = nx.circular_layout(G4)
    nx.draw(G4, pos4, ax=axes[1, 0], with_labels=True, node_color='yellow', 
            node_size=500, font_size=16, font_weight='bold')
    axes[1, 0].set_title('Complete Graph K₅')
    
    # 5. Bipartite graph
    G5 = nx.Graph()
    G5.add_nodes_from([1, 2, 3], bipartite=0)  # Set A
    G5.add_nodes_from([4, 5, 6, 7], bipartite=1)  # Set B
    G5.add_edges_from([(1, 4), (1, 5), (2, 5), (2, 6), (3, 6), (3, 7)])
    pos5 = {}
    pos5.update({n: (0, i) for i, n in enumerate([1, 2, 3])})
    pos5.update({n: (2, i) for i, n in enumerate([4, 5, 6, 7])})
    nx.draw(G5, pos5, ax=axes[1, 1], with_labels=True, node_color='orange', 
            node_size=500, font_size=16, font_weight='bold')
    axes[1, 1].set_title('Bipartite Graph')
    
    # 6. Tree
    G6 = nx.balanced_tree(2, 3)  # Binary tree of height 3
    pos6 = nx.spring_layout(G6)
    nx.draw(G6, pos6, ax=axes[1, 2], with_labels=True, node_color='pink', 
            node_size=500, font_size=16, font_weight='bold')
    axes[1, 2].set_title('Binary Tree')
    
    plt.tight_layout()
    plt.show()
    
    return G1, G2, G3, G4, G5, G6

graphs = create_example_graphs()
```

### Graph Properties

#### **Degree**
- **Degree**: Number of edges incident to a vertex
- **In-degree**: Number of incoming edges (directed graphs)
- **Out-degree**: Number of outgoing edges (directed graphs)

#### **Paths and Connectivity**
- **Path**: Sequence of vertices connected by edges
- **Cycle**: Path that starts and ends at the same vertex
- **Connected**: Path exists between every pair of vertices
- **Strongly Connected**: Directed graph where path exists in both directions

```python
def analyze_graph_properties(G):
    """Analyze basic properties of a graph"""
    print(f"Graph Analysis:")
    print(f"Number of nodes: {G.number_of_nodes()}")
    print(f"Number of edges: {G.number_of_edges()}")
    print(f"Is connected: {nx.is_connected(G) if not G.is_directed() else nx.is_strongly_connected(G)}")
    
    # Degree analysis
    degrees = dict(G.degree())
    print(f"Degrees: {degrees}")
    print(f"Average degree: {np.mean(list(degrees.values())):.2f}")
    
    # Diameter and radius
    if nx.is_connected(G):
        diameter = nx.diameter(G)
        radius = nx.radius(G)
        print(f"Diameter: {diameter}")
        print(f"Radius: {radius}")
    
    # Clustering coefficient
    clustering = nx.average_clustering(G)
    print(f"Average clustering coefficient: {clustering:.3f}")
    
    return degrees

# Analyze the simple graph from above
G = nx.Graph()
G.add_edges_from([(1, 2), (2, 3), (3, 4), (4, 1), (2, 4)])
properties = analyze_graph_properties(G)
```

---

## Graph Representations

### Adjacency Matrix
A[i,j] = 1 if edge (i,j) exists, 0 otherwise.

### Adjacency List
For each vertex, store list of its neighbors.

### Edge List
Store all edges as pairs (or triples for weighted graphs).

```python
def graph_representations():
    """Demonstrate different graph representations"""
    
    # Create a simple graph
    edges = [(0, 1), (1, 2), (2, 3), (3, 0), (1, 3)]
    n_nodes = 4
    
    # 1. Adjacency Matrix
    adj_matrix = np.zeros((n_nodes, n_nodes), dtype=int)
    for i, j in edges:
        adj_matrix[i, j] = 1
        adj_matrix[j, i] = 1  # Undirected graph
    
    print("Adjacency Matrix:")
    print(adj_matrix)
    
    # 2. Adjacency List
    adj_list = defaultdict(list)
    for i, j in edges:
        adj_list[i].append(j)
        adj_list[j].append(i)  # Undirected graph
    
    print("\nAdjacency List:")
    for node, neighbors in adj_list.items():
        print(f"Node {node}: {neighbors}")
    
    # 3. Edge List
    print(f"\nEdge List: {edges}")
    
    # Memory comparison
    print(f"\nMemory Usage:")
    print(f"Adjacency Matrix: O(V²) = O({n_nodes}²) = {n_nodes**2} entries")
    print(f"Adjacency List: O(V + E) = O({n_nodes} + {len(edges)}) = {n_nodes + len(edges)} entries")
    print(f"Edge List: O(E) = O({len(edges)}) = {len(edges)} entries")
    
    return adj_matrix, adj_list, edges

representations = graph_representations()
```

### Sparse vs Dense Graphs
- **Sparse**: |E| << |V|² (few edges)
- **Dense**: |E| ≈ |V|² (many edges)

```python
def compare_sparse_dense():
    """Compare sparse and dense graph representations"""
    
    # Sparse graph (tree-like)
    n_sparse = 100
    G_sparse = nx.random_tree(n_sparse)
    
    # Dense graph (nearly complete)
    n_dense = 20
    G_dense = nx.erdos_renyi_graph(n_dense, 0.8)
    
    print("Sparse Graph (Tree):")
    print(f"Nodes: {G_sparse.number_of_nodes()}")
    print(f"Edges: {G_sparse.number_of_edges()}")
    print(f"Density: {nx.density(G_sparse):.4f}")
    
    print("\nDense Graph:")
    print(f"Nodes: {G_dense.number_of_nodes()}")
    print(f"Edges: {G_dense.number_of_edges()}")
    print(f"Density: {nx.density(G_dense):.4f}")
    
    # Visualization
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Sparse graph
    pos_sparse = nx.spring_layout(G_sparse)
    nx.draw(G_sparse, pos_sparse, ax=axes[0], node_size=20, node_color='blue', 
            with_labels=False, edge_color='gray', alpha=0.7)
    axes[0].set_title(f'Sparse Graph (Density: {nx.density(G_sparse):.3f})')
    
    # Dense graph
    pos_dense = nx.spring_layout(G_dense)
    nx.draw(G_dense, pos_dense, ax=axes[1], node_size=100, node_color='red', 
            with_labels=True, edge_color='gray', alpha=0.7)
    axes[1].set_title(f'Dense Graph (Density: {nx.density(G_dense):.3f})')
    
    plt.tight_layout()
    plt.show()

compare_sparse_dense()
```

---

## Graph Algorithms

### Breadth-First Search (BFS)
Explores graph level by level from starting vertex.

### Depth-First Search (DFS)
Explores as far as possible along each branch before backtracking.

```python
def implement_graph_traversals():
    """Implement BFS and DFS algorithms"""
    
    class Graph:
        def __init__(self):
            self.graph = defaultdict(list)
        
        def add_edge(self, u, v):
            self.graph[u].append(v)
            self.graph[v].append(u)  # Undirected
        
        def bfs(self, start):
            """Breadth-First Search"""
            visited = set()
            queue = deque([start])
            bfs_order = []
            
            while queue:
                vertex = queue.popleft()
                if vertex not in visited:
                    visited.add(vertex)
                    bfs_order.append(vertex)
                    
                    # Add unvisited neighbors to queue
                    for neighbor in self.graph[vertex]:
                        if neighbor not in visited:
                            queue.append(neighbor)
            
            return bfs_order
        
        def dfs(self, start):
            """Depth-First Search"""
            visited = set()
            dfs_order = []
            
            def dfs_recursive(vertex):
                visited.add(vertex)
                dfs_order.append(vertex)
                
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        dfs_recursive(neighbor)
            
            dfs_recursive(start)
            return dfs_order
    
    # Create example graph
    g = Graph()
    edges = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5), (2, 6)]
    for u, v in edges:
        g.add_edge(u, v)
    
    # Perform traversals
    bfs_result = g.bfs(0)
    dfs_result = g.dfs(0)
    
    print("Graph Traversals:")
    print(f"BFS from node 0: {bfs_result}")
    print(f"DFS from node 0: {dfs_result}")
    
    # Visualize the graph and traversal orders
    G = nx.Graph()
    G.add_edges_from(edges)
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    pos = nx.spring_layout(G)
    
    # BFS visualization
    nx.draw(G, pos, ax=axes[0], with_labels=True, node_color='lightblue', 
            node_size=500, font_size=16, font_weight='bold')
    axes[0].set_title(f'BFS Order: {bfs_result}')
    
    # DFS visualization
    nx.draw(G, pos, ax=axes[1], with_labels=True, node_color='lightcoral', 
            node_size=500, font_size=16, font_weight='bold')
    axes[1].set_title(f'DFS Order: {dfs_result}')
    
    plt.tight_layout()
    plt.show()
    
    return g, bfs_result, dfs_result

graph_traversals = implement_graph_traversals()
```

### Shortest Path Algorithms

#### **Dijkstra's Algorithm**
Finds shortest paths from source to all vertices (non-negative weights).

#### **Bellman-Ford Algorithm**
Handles negative weights, detects negative cycles.

#### **Floyd-Warshall Algorithm**
All-pairs shortest paths.

```python
def shortest_path_algorithms():
    """Implement and compare shortest path algorithms"""
    
    def dijkstra(graph, start):
        """Dijkstra's algorithm for shortest paths"""
        import heapq
        
        distances = {node: float('inf') for node in graph}
        distances[start] = 0
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            for neighbor, weight in graph[current].items():
                distance = current_dist + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))
        
        return distances
    
    # Create weighted graph
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'A': 4, 'C': 1, 'D': 5},
        'C': {'A': 2, 'B': 1, 'D': 8, 'E': 10},
        'D': {'B': 5, 'C': 8, 'E': 2},
        'E': {'C': 10, 'D': 2}
    }
    
    # Run Dijkstra from node 'A'
    distances = dijkstra(graph, 'A')
    
    print("Shortest Path Distances from A:")
    for node, dist in distances.items():
        print(f"A → {node}: {dist}")
    
    # Visualize with NetworkX
    G = nx.Graph()
    for node, neighbors in graph.items():
        for neighbor, weight in neighbors.items():
            G.add_edge(node, neighbor, weight=weight)
    
    plt.figure(figsize=(10, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', 
            node_size=1000, font_size=16, font_weight='bold')
    
    # Draw edge labels (weights)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels)
    
    plt.title("Weighted Graph for Shortest Path")
    plt.show()
    
    return distances

shortest_paths = shortest_path_algorithms()
```

---

## Spectral Graph Theory

### Graph Laplacian
L = D - A where D is degree matrix and A is adjacency matrix.

### Properties
- L is positive semidefinite
- Smallest eigenvalue is 0
- Number of 0 eigenvalues = number of connected components
- Second smallest eigenvalue (Fiedler value) measures connectivity

```python
def spectral_graph_analysis():
    """Analyze graphs using spectral methods"""
    
    def compute_graph_laplacian(G):
        """Compute the graph Laplacian matrix"""
        A = nx.adjacency_matrix(G).toarray()
        D = np.diag(np.sum(A, axis=1))
        L = D - A
        return L, A, D
    
    def analyze_spectrum(L, G):
        """Analyze eigenvalues and eigenvectors of Laplacian"""
        eigenvals, eigenvecs = np.linalg.eigh(L)
        
        print(f"Graph Spectral Analysis:")
        print(f"Number of nodes: {G.number_of_nodes()}")
        print(f"Number of edges: {G.number_of_edges()}")
        print(f"Number of connected components: {nx.number_connected_components(G)}")
        print(f"Eigenvalues: {eigenvals[:5].round(3)}")  # First 5
        print(f"Fiedler value (algebraic connectivity): {eigenvals[1]:.3f}")
        
        return eigenvals, eigenvecs
    
    # Create different types of graphs
    graphs = {
        'Path': nx.path_graph(10),
        'Cycle': nx.cycle_graph(10),
        'Complete': nx.complete_graph(6),
        'Star': nx.star_graph(9),
        'Disconnected': nx.union(nx.complete_graph(3), nx.complete_graph(3))
    }
    
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    axes = axes.flatten()
    
    for i, (name, G) in enumerate(graphs.items()):
        if i >= 5:  # Only plot first 5
            break
            
        L, A, D = compute_graph_laplacian(G)
        eigenvals, eigenvecs = analyze_spectrum(L, G)
        
        # Plot graph
        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=axes[i], with_labels=True, node_color='lightblue', 
                node_size=300, font_size=10)
        axes[i].set_title(f'{name} Graph\nFiedler: {eigenvals[1]:.3f}')
    
    # Plot eigenvalue spectrum comparison
    axes[5].set_title('Eigenvalue Spectra')
    for name, G in graphs.items():
        L, _, _ = compute_graph_laplacian(G)
        eigenvals, _ = np.linalg.eigh(L)
        axes[5].plot(eigenvals, 'o-', label=name, alpha=0.7)
    
    axes[5].set_xlabel('Eigenvalue Index')
    axes[5].set_ylabel('Eigenvalue')
    axes[5].legend()
    axes[5].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

spectral_graph_analysis()
```

### Spectral Clustering
Use eigenvectors of graph Laplacian for clustering.

```python
def spectral_clustering_demo():
    """Demonstrate spectral clustering"""
    from sklearn.cluster import SpectralClustering
    from sklearn.datasets import make_blobs
    
    # Generate data with clear clusters
    X, y_true = make_blobs(n_samples=100, centers=3, n_features=2, 
                          random_state=42, cluster_std=1.5)
    
    # Build k-nearest neighbor graph
    from sklearn.neighbors import kneighbors_graph
    knn_graph = kneighbors_graph(X, n_neighbors=10, mode='connectivity')
    
    # Apply spectral clustering
    spectral = SpectralClustering(n_clusters=3, affinity='precomputed', 
                                 random_state=42)
    y_pred = spectral.fit_predict(knn_graph)
    
    # Visualize results
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    # Original data
    axes[0].scatter(X[:, 0], X[:, 1], c=y_true, cmap='viridis', s=50)
    axes[0].set_title('True Clusters')
    axes[0].grid(True, alpha=0.3)
    
    # KNN graph
    G = nx.from_scipy_sparse_matrix(knn_graph)
    pos = {i: X[i] for i in range(len(X))}
    nx.draw(G, pos, ax=axes[1], node_color=y_true, node_size=50, 
            cmap=plt.cm.viridis, with_labels=False, edge_color='gray', alpha=0.5)
    axes[1].set_title('K-NN Graph')
    
    # Spectral clustering result
    axes[2].scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', s=50)
    axes[2].set_title('Spectral Clustering Result')
    axes[2].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Accuracy
    from sklearn.metrics import adjusted_rand_score
    ari = adjusted_rand_score(y_true, y_pred)
    print(f"Adjusted Rand Index: {ari:.3f}")

spectral_clustering_demo()
```

---

## Random Graphs

### Erdős–Rényi Model
G(n, p): n vertices, each edge exists with probability p.

### Barabási–Albert Model
Preferential attachment: new nodes connect to existing nodes with probability proportional to their degree.

```python
def random_graph_models():
    """Compare different random graph models"""
    
    n = 100  # Number of nodes
    
    # 1. Erdős–Rényi random graph
    p = 0.05
    G_er = nx.erdos_renyi_graph(n, p)
    
    # 2. Barabási–Albert preferential attachment
    m = 2  # Number of edges to attach from new node
    G_ba = nx.barabasi_albert_graph(n, m)
    
    # 3. Watts-Strogatz small-world
    k = 4  # Each node connected to k nearest neighbors
    p_rewire = 0.3
    G_ws = nx.watts_strogatz_graph(n, k, p_rewire)
    
    # Analyze properties
    graphs = {'Erdős–Rényi': G_er, 'Barabási–Albert': G_ba, 'Watts-Strogatz': G_ws}
    
    print("Random Graph Model Comparison:")
    print("-" * 50)
    
    for name, G in graphs.items():
        degrees = [d for n, d in G.degree()]
        clustering = nx.average_clustering(G)
        
        if nx.is_connected(G):
            path_length = nx.average_shortest_path_length(G)
        else:
            # Use largest connected component
            largest_cc = max(nx.connected_components(G), key=len)
            subgraph = G.subgraph(largest_cc)
            path_length = nx.average_shortest_path_length(subgraph)
        
        print(f"{name}:")
        print(f"  Average degree: {np.mean(degrees):.2f}")
        print(f"  Degree std: {np.std(degrees):.2f}")
        print(f"  Clustering coefficient: {clustering:.3f}")
        print(f"  Average path length: {path_length:.3f}")
        print()
    
    # Visualize degree distributions
    fig, axes = plt.subplots(2, 3, figsize=(18, 12))
    
    for i, (name, G) in enumerate(graphs.items()):
        # Graph visualization
        pos = nx.spring_layout(G, k=0.5, iterations=50)
        nx.draw(G, pos, ax=axes[0, i], node_size=20, node_color='blue', 
                edge_color='gray', alpha=0.6, with_labels=False)
        axes[0, i].set_title(f'{name} Graph')
        
        # Degree distribution
        degrees = [d for n, d in G.degree()]
        axes[1, i].hist(degrees, bins=20, alpha=0.7, color='skyblue', edgecolor='black')
        axes[1, i].set_xlabel('Degree')
        axes[1, i].set_ylabel('Frequency')
        axes[1, i].set_title(f'{name} Degree Distribution')
        axes[1, i].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

random_graph_models()
```

---

## Graph Neural Networks

### Message Passing Framework
1. **Message**: Compute messages between connected nodes
2. **Aggregate**: Combine messages from neighbors
3. **Update**: Update node representations

```python
def simple_gnn_implementation():
    """Implement a simple Graph Neural Network"""
    
    class SimpleGNN:
        def __init__(self, input_dim, hidden_dim, output_dim):
            self.input_dim = input_dim
            self.hidden_dim = hidden_dim
            self.output_dim = output_dim
            
            # Initialize weights (simplified)
            np.random.seed(42)
            self.W1 = np.random.randn(input_dim, hidden_dim) * 0.1
            self.W2 = np.random.randn(hidden_dim, output_dim) * 0.1
        
        def message_passing(self, X, A):
            """Simple message passing: aggregate neighbor features"""
            # Normalize adjacency matrix
            D = np.diag(np.sum(A, axis=1))
            D_inv_sqrt = np.diag(1.0 / np.sqrt(np.diag(D) + 1e-6))
            A_norm = D_inv_sqrt @ A @ D_inv_sqrt
            
            # First layer: message passing + activation
            H1 = np.tanh(A_norm @ X @ self.W1)
            
            # Second layer: output
            H2 = A_norm @ H1 @ self.W2
            
            return H2
        
        def forward(self, X, A):
            """Forward pass through GNN"""
            return self.message_passing(X, A)
    
    # Create example graph and features
    G = nx.karate_club_graph()  # Famous social network
    A = nx.adjacency_matrix(G).toarray()
    
    # Random node features
    n_nodes = G.number_of_nodes()
    X = np.random.randn(n_nodes, 4)  # 4-dimensional features
    
    # Initialize GNN
    gnn = SimpleGNN(input_dim=4, hidden_dim=8, output_dim=2)
    
    # Forward pass
    output = gnn.forward(X, A)
    
    print("Simple GNN Implementation:")
    print(f"Input shape: {X.shape}")
    print(f"Output shape: {output.shape}")
    print(f"Graph: {G.number_of_nodes()} nodes, {G.number_of_edges()} edges")
    
    # Visualize original graph and learned embeddings
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    
    # Original graph
    pos = nx.spring_layout(G)
    nx.draw(G, pos, ax=axes[0], with_labels=True, node_color='lightblue', 
            node_size=300, font_size=8)
    axes[0].set_title('Karate Club Graph')
    
    # Learned embeddings (2D projection)
    axes[1].scatter(output[:, 0], output[:, 1], c=range(n_nodes), 
                   cmap='viridis', s=100)
    for i, (x, y) in enumerate(output):
        axes[1].annotate(str(i), (x, y), xytext=(5, 5), 
                        textcoords='offset points', fontsize=8)
    axes[1].set_xlabel('Embedding Dimension 1')
    axes[1].set_ylabel('Embedding Dimension 2')
    axes[1].set_title('Learned Node Embeddings')
    axes[1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    return gnn, output

gnn_demo = simple_gnn_implementation()
```

---

## Applications in ML/AI

### 1. **Social Network Analysis**
```python
def social_network_analysis():
    """Analyze social networks using graph metrics"""
    
    # Create a social network (using Karate Club as example)
    G = nx.karate_club_graph()
    
    # Calculate centrality measures
    degree_centrality = nx.degree_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    eigenvector_centrality = nx.eigenvector_centrality(G)
    
    # Find most influential nodes
    most_degree = max(degree_centrality, key=degree_centrality.get)
    most_betweenness = max(betweenness_centrality, key=betweenness_centrality.get)
    
    print("Social Network Analysis:")
    print(f"Most connected node (degree): {most_degree}")
    print(f"Most influential node (betweenness): {most_betweenness}")
    
    # Community detection
    communities = nx.community.greedy_modularity_communities(G)
    print(f"Number of communities: {len(communities)}")
    
    # Visualize with centrality-based node sizes
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    
    # Node sizes based on degree centrality
    node_sizes = [degree_centrality[node] * 1000 for node in G.nodes()]
    
    # Node colors based on communities
    node_colors = []
    for node in G.nodes():
        for i, community in enumerate(communities):
            if node in community:
                node_colors.append(i)
                break
    
    nx.draw(G, pos, node_size=node_sizes, node_color=node_colors, 
            cmap='Set3', with_labels=True, font_size=8, font_weight='bold')
    plt.title('Social Network: Node size = Degree Centrality, Color = Community')
    plt.show()

social_network_analysis()
```

### 2. **Knowledge Graph Reasoning**
```python
def knowledge_graph_example():
    """Create and analyze a simple knowledge graph"""
    
    # Create knowledge graph
    KG = nx.DiGraph()
    
    # Add entities and relationships
    facts = [
        ('Python', 'is_a', 'Programming_Language'),
        ('Python', 'used_for', 'Machine_Learning'),
        ('Machine_Learning', 'is_a', 'AI_Technique'),
        ('Neural_Networks', 'is_a', 'Machine_Learning'),
        ('Deep_Learning', 'is_a', 'Neural_Networks'),
        ('Transformer', 'is_a', 'Deep_Learning'),
        ('GPT', 'is_a', 'Transformer'),
        ('BERT', 'is_a', 'Transformer'),
    ]
    
    for head, relation, tail in facts:
        KG.add_edge(head, tail, relation=relation)
    
    # Analyze knowledge graph
    print("Knowledge Graph Analysis:")
    print(f"Entities: {KG.number_of_nodes()}")
    print(f"Relations: {KG.number_of_edges()}")
    
    # Find paths (reasoning)
    try:
        path = nx.shortest_path(KG, 'Python', 'GPT')
        print(f"Path from Python to GPT: {' → '.join(path)}")
    except nx.NetworkXNoPath:
        print("No path found from Python to GPT")
    
    # Visualize knowledge graph
    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(KG, k=2, iterations=50)
    
    nx.draw(KG, pos, with_labels=True, node_color='lightcoral', 
            node_size=1000, font_size=8, font_weight='bold', 
            arrows=True, arrowsize=20, edge_color='gray')
    
    # Add edge labels (relations)
    edge_labels = nx.get_edge_attributes(KG, 'relation')
    nx.draw_networkx_edge_labels(KG, pos, edge_labels, font_size=6)
    
    plt.title('Knowledge Graph: AI/ML Domain')
    plt.show()

knowledge_graph_example()
```

### 3. **Recommendation Systems**
```python
def recommendation_system_graph():
    """Build recommendation system using bipartite graph"""
    
    # Create user-item bipartite graph
    B = nx.Graph()
    
    # Users and items
    users = ['U1', 'U2', 'U3', 'U4', 'U5']
    items = ['Movie_A', 'Movie_B', 'Movie_C', 'Movie_D', 'Movie_E']
    
    # Add nodes with bipartite attribute
    B.add_nodes_from(users, bipartite=0)
    B.add_nodes_from(items, bipartite=1)
    
    # Add edges (user-item interactions)
    interactions = [
        ('U1', 'Movie_A'), ('U1', 'Movie_B'),
        ('U2', 'Movie_A'), ('U2', 'Movie_C'),
        ('U3', 'Movie_B'), ('U3', 'Movie_C'), ('U3', 'Movie_D'),
        ('U4', 'Movie_C'), ('U4', 'Movie_D'),
        ('U5', 'Movie_D'), ('U5', 'Movie_E')
    ]
    
    B.add_edges_from(interactions)
    
    # Project to user-user similarity graph
    user_nodes = {n for n, d in B.nodes(data=True) if d['bipartite'] == 0}
    user_graph = nx.bipartite.projected_graph(B, user_nodes)
    
    # Calculate user similarities (based on common items)
    similarities = {}
    for u1 in users:
        for u2 in users:
            if u1 != u2:
                common_items = len(set(B.neighbors(u1)) & set(B.neighbors(u2)))
                total_items = len(set(B.neighbors(u1)) | set(B.neighbors(u2)))
                similarity = common_items / total_items if total_items > 0 else 0
                similarities[(u1, u2)] = similarity
    
    print("Recommendation System Analysis:")
    print("User-User Similarities:")
    for (u1, u2), sim in similarities.items():
        if sim > 0:
            print(f"{u1} - {u2}: {sim:.3f}")
    
    # Visualize bipartite graph
    plt.figure(figsize=(12, 8))
    pos = {}
    pos.update({user: (0, i) for i, user in enumerate(users)})
    pos.update({item: (2, i) for i, item in enumerate(items)})
    
    nx.draw(B, pos, with_labels=True, node_color=['lightblue']*len(users) + ['lightcoral']*len(items),
            node_size=1000, font_size=8, font_weight='bold')
    plt.title('User-Item Bipartite Graph for Recommendations')
    plt.show()

recommendation_system_graph()
```

---

## Practice Problems

### Problem 1: Graph Coloring
Find the chromatic number of a cycle graph C₅.

**Solution:**
A cycle of odd length requires 3 colors. For C₅: vertices can be colored with pattern 1-2-3-1-2, so χ(C₅) = 3.

### Problem 2: Shortest Path
Find shortest path from A to E in weighted graph using Dijkstra's algorithm.

**Solution:**
Apply Dijkstra's algorithm step by step, maintaining priority queue of unvisited vertices with their distances.

### Problem 3: Graph Isomorphism
Determine if two graphs are isomorphic by comparing their structural properties.

**Solution:**
Check invariants: number of vertices, edges, degree sequence, diameter, etc. If all match, graphs might be isomorphic.

---

## 🎯 Key Takeaways

1. **Graphs Model Relationships**: Essential for representing complex data structures
2. **Algorithms are Fundamental**: BFS, DFS, shortest paths are building blocks
3. **Spectral Methods are Powerful**: Eigenvalues reveal graph structure
4. **Random Graphs Model Reality**: Different models capture different network properties
5. **GNNs are Revolutionary**: Learning on graph-structured data
6. **Applications are Everywhere**: Social networks, knowledge graphs, recommendations

---

## 📚 Next Steps

After mastering graph theory, proceed to:
1. **Advanced Graph Algorithms** - Maximum flow, matching, planarity
2. **Network Science** - Scale-free networks, epidemic models
3. **Algebraic Graph Theory** - Group theory and graph automorphisms
4. **Geometric Graph Theory** - Graphs embedded in geometric spaces

---

## 🔗 Resources

- **NetworkX Documentation** - Python graph library
- **Graph Theory by Diestel** - Comprehensive textbook
- **Networks by Newman** - Network science perspective
- **PyTorch Geometric** - Graph neural networks
- **Deep Graph Library (DGL)** - Scalable GNN framework

---

*Graph theory provides the mathematical foundation for understanding networks and relationships in data. Master it to unlock the power of graph-based ML/AI methods!*