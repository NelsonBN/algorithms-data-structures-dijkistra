import matplotlib.pyplot as plt # pip install matplotlib
import networkx as nx # pip install networkx

# graph = {
#     'A': { 'B': 1, 'C': 4},
#     'B': { 'A': 1, 'C': 2, 'D': 5 },
#     'C': { 'A': 4, 'B': 2, 'D': 1 },
#     'D': { 'B': 5, 'C': 1 }
# }

graph = {
    "A": {"B": 3, "D": 4, "S": 7},
    "B": {"A": 3, "D": 4, "S": 2, "H": 1},
    "C": {"S": 3, "L": 2},
    "D": {"A": 4, "B": 4, "F": 5},
    "E": {"G": 2, "K": 5},
    "F": {"D": 5, "H": 3},
    "G": {"E": 2, "H": 2},
    "H": {"B": 1, "F": 3, "G": 2},
    "I": {"J": 6, "K": 4, "L": 4},
    "J": {"I": 6, "K": 4, "L": 4},
    "K": {"E": 5, "I": 4, "J": 4},
    "L": {"C": 2, "I": 4, "J": 4},
    "S": {"A": 7, "B": 2, "C": 3}
}


# Preparing graph for visualization
plt.rcParams['toolbar'] = 'None'
plt.figure(figsize=(5, 5))

graphObj = nx.Graph()

# Add nodes
for node, neighbors in graph.items():
    for neighbor, distance in neighbors.items():
        graphObj.add_edge(node, neighbor, distance=distance)


# Dijkstra's algorithm
path = nx.shortest_path(graphObj, source="S", target="E", weight="distance")
print(path)


# Draw nodes
pos = nx.spring_layout(graphObj, k=0.5811, seed=42)
nx.draw(
    graphObj,
    pos = pos,
    with_labels = True,
    node_size = 500,
    node_color = "skyblue",
    font_size = 10,
    width = 1,
    edge_color = "gray")

# Draw path
pathEdges = [(path[i], path[i+1]) for i in range(len(path)-1)]
nx.draw_networkx_nodes(
    graphObj,
    pos = pos,
    nodelist = path,
    node_color = "lightgreen")
nx.draw_networkx_edges(
    graphObj,
    pos = pos,
    edgelist = pathEdges,
    edge_color = "red",
    width = 1)
# Start node
nx.draw_networkx_nodes(
    graphObj,
    pos = pos,
    nodelist = [path[0]],
    node_color = "yellow")
# End node
nx.draw_networkx_nodes(
    graphObj,
    pos = pos,
    nodelist = [path[-1]],
    node_color = "orange")


# Draw edge labels
labels = nx.get_edge_attributes(graphObj, 'distance')
nx.draw_networkx_edge_labels(
    graphObj,
    pos = pos,
    edge_labels = labels,
    font_size = 10)


plt.show()
