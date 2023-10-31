# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()

# nodes = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]
# G.add_nodes_from(nodes)

# edges = [
#     ("Mchinji", "Kasungu", 141), 
#     ("Mchinji", "Lilongwe", 109), 
#     ("Lilongwe", "Dedza", 92), 
#     ("Lilongwe", "Dowa", 55), 
#     ("Kasungu", "Dowa", 117),
#     ("Kasungu", "Ntchisi", 66),
#     ("Dowa", "Ntchisi", 38),
#     ("Dowa", "Salima", 67),
#     ("Dedza", "Ntcheu", 74),
#     ("Dedza", "Salima", 96),
#     ("Nkhotakota", "Ntchisi", 66),
#     ("Nkhotakota", "Salima", 112)
#         ]
# G.add_weighted_edges_from(edges)

# pos = nx.circular_layout(G)  # Positions nodes in a circular layout
# labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights as labels

# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=16, font_weight='bold')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

# plt.title("Simple Weighted Graph")
# plt.show()

# import networkx as nx
# import matplotlib.pyplot as plt

# G = nx.Graph()

# nodes = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]
# G.add_nodes_from(nodes)

# edges = [
#     ("Mchinji", "Kasungu", 141),
#     ("Mchinji", "Lilongwe", 109),
#     ("Lilongwe", "Dedza", 92),
#     ("Lilongwe", "Dowa", 55),
#     ("Kasungu", "Dowa", 117),
#     ("Kasungu", "Ntchisi", 66),
#     ("Dowa", "Ntchisi", 38),
#     ("Dowa", "Salima", 67),
#     ("Dedza", "Ntcheu", 74),
#     ("Dedza", "Salima", 96),
#     ("Nkhotakota", "Ntchisi", 66),
#     ("Nkhotakota", "Salima", 112)
# ]
# G.add_weighted_edges_from(edges)

# # Print edges and their associated weights
# for edge in G.edges(data=True):
#     source, target, weight = edge
#     print(f"Edge: {source} - {target}, Weight: {weight['weight']}")

# pos = nx.circular_layout(G)  # Positions nodes in a circular layout
# labels = nx.get_edge_attributes(G, 'weight')  # Get edge weights as labels

# nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=16, font_weight='bold')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=12)

# plt.title("Simple Weighted Graph")
# plt.show()

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ["Mchinji", "Lilongwe", "Kasungu", "Dedza", "Ntcheu", "Salima", "Dowa", "Ntchisi", "Nkhotakota"]
G.add_nodes_from(nodes)

edges = [
    ("Mchinji", "Kasungu", 141),
    ("Mchinji", "Lilongwe", 109),
    ("Lilongwe", "Dedza", 92),
    ("Lilongwe", "Dowa", 55),
    ("Kasungu", "Dowa", 117),
    ("Kasungu", "Ntchisi", 66),
    ("Dowa", "Ntchisi", 38),
    ("Dowa", "Salima", 67),
    ("Dedza", "Ntcheu", 74),
    ("Dedza", "Salima", 96),
    ("Nkhotakota", "Ntchisi", 66),
    ("Nkhotakota", "Salima", 112)
]
G.add_weighted_edges_from(edges)

# Find all shortest paths between nodes and update the edges
for source in nodes:
    for target in nodes:
        if source != target:
            paths = list(nx.all_shortest_paths(G, source=source, target=target))
            if paths:
                G[source][target]['paths'] = paths

# Print edges with shortest paths
for source, target, data in G.edges(data=True):
    if 'paths' in data:
        print(f"Edge: {source} - {target}")
        for path in data['paths']:
            print(f"Shortest Path: {path}")

pos = nx.circular_layout(G)  # Positions nodes in a circular layout

nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=16, font_weight='bold')

plt.title("Weighted Graph with Shortest Paths")
plt.show()
