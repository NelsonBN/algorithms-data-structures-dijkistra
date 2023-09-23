from collections import defaultdict
import heapq

def dijkistra(graph, source):
    distances = {}
    queue = [(0, source, source)]

    while len(distances) < len(graph):
        cost, cur, prev = heapq.heappop(queue)

        if cur in distances:
            continue

        distances[cur] = (cost, prev)

        for neighbor, neighbor_cost in graph[cur].items():
            neighbor_cumulative_cost = cost + neighbor_cost
            heapq.heappush(queue, (neighbor_cumulative_cost, neighbor, cur))

    return distances



# graph = {
#     'A': { 'B': 5, 'C': 1},
#     'B': { 'D': 2, 'B': 4, 'E': 4 },
#     'C': { 'E': 5, 'B': 2, 'D': 5 },
#     'D': { 'E': 2 },
#     'E': { }
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


print(graph)
print(dijkistra(graph, "A"))