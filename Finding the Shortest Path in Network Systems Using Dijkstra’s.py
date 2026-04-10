import networkx as nx
import matplotlib.pyplot as plt

def visualize_graph(G, path=None):
    pos = nx.spring_layout(G, seed=42)  # fixed layout for consistency
    
    plt.figure(figsize=(10, 7))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=14, font_weight='bold', arrows=True)
    
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=12)
    
    if path:
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='green', width=3, arrows=True)
    
    plt.title("Directed Weighted Graph with Shortest Path Highlighted", fontsize=16)
    plt.axis('off')
    plt.show()

def add_edge(G):
    while True:
        u = input("Enter the start node of the edge: ").strip()
        v = input("Enter the end node of the edge: ").strip()
        if u not in G.nodes or v not in G.nodes:
            print("One or both nodes do not exist. Please add them first")
            return
        try:
            weight = int(input("Enter the weight of the edge: "))
            G.add_edge(u, v, weight=weight)
            print(f"Edge from {u} to {v} with weight {weight} added.")
            break
        except ValueError:
            print("Invalid weight. Please enter an integer.")

def remove_edge(G):
    u = input("Enter the start node of the edge to remove: ").strip()
    v = input("Enter the end node of the edge to remove: ").strip()
    if G.has_edge(u, v):
        G.remove_edge(u, v)
        print(f"Edge from {u} to {v} removed.")
    else:
        print("Edge does not exist.")

def add_node(G):
    node = input("Enter the name of the node to add: ").strip()
    if node in G.nodes:
        print(f"Node {node} already exists.")
    else:
        G.add_node(node)
        print(f"Node {node} added.")

def remove_node(G):
    node = input("Enter the name of the node to remove: ").strip()
    if node in G.nodes:
        G.remove_node(node)
        print(f"Node {node} removed.")
    else:
        print("Node does not exist.")

def find_shortest_path(G):
    start_node = input("Enter the start node: ").strip()
    end_node = input("Enter the end node: ").strip()
    if start_node not in G.nodes or end_node not in G.nodes:
        print("One or both nodes do not exist in the graph.")
        return None
    if start_node == end_node:
        print("Start and end nodes are the same; the shortest path is the node itself.")
        return [start_node]
    try:
        path = nx.dijkstra_path(G, start_node, end_node)
        print(f"The shortest path from {start_node} to {end_node} is: {' -> '.join(path)}")
        return path
    except nx.NetworkXNoPath:
        print("No path found between the specified nodes.")
        return None

def input_graph():
    G = nx.DiGraph()
    print("Enter nodes for the graph. Type 'done' when finished:")
    while True:
        node = input("Enter node name: ").strip()
        if node.lower() == 'done':
            break
        if node == '':
            continue
        if node in G.nodes:
            print(f"Node {node} already exists.")
        else:
            G.add_node(node)
            print(f"Node {node} added.")
    print("\nNow enter edges. Type 'done' when finished:")
    while True:
        u = input("Enter start node of edge: ").strip()
        if u.lower() == 'done':
            break
        v = input("Enter end node of edge: ").strip()
        if v.lower() == 'done':
            break
        if u not in G.nodes or v not in G.nodes:
            print("One or both nodes do not exist. Add nodes first.")
            continue
        try:
            weight = int(input("Enter weight of edge: "))
            G.add_edge(u, v, weight=weight)
            print(f"Edge from {u} to {v} with weight {weight} added.")
        except ValueError:
            print("Invalid weight. Please enter an integer.")
    return G

def main():
    print("Create your directed weighted graph")
    G = input_graph()
    
    while True:
        print("\nMenu:")
        print("1: Find shortest path")
        print("2: Add node")
        print("3: Remove node")
        print("4: Add edge")
        print("5: Remove edge")
        print("6: Visualize graph")
        print("7: Exit")
        choice = input("Choose an option: ").strip()
        
        if choice == '1':
            path = find_shortest_path(G)
            # After shortest path found, visualize with path highlighted
            visualize_graph(G, path)
        elif choice == '2':
            add_node(G)
        elif choice == '3':
            remove_node(G)
        elif choice == '4':
            add_edge(G)
        elif choice == '5':
            remove_edge(G)
        elif choice == '6':
            visualize_graph(G)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid option, please choose again.")

if __name__ == "__main__":
    main()

