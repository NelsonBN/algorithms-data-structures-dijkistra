from collections import defaultdict, deque
import heapq


def dijkistra1(graph, source):
    # Structure to store the nodes already visited, we use a HashTable because has a O(1) complexity
    visited = set()

    # Structure to store the distances from the origin to each node, we use a Dictionary because has a O(1) complexity
    #    When we find a non-existent node in the dictionary, it will be considered as infinity
    distances = defaultdict(lambda: float('inf'))

    # Added the distance from the origin to itself
    distances[source] = 0

    # Queue to get the next node with the lowest cost. We will use as a min-heap to get the lowest cost. Min-heap has a O(log n) complexity
    queue = [(0, source)]

    # While the queue is not empty and we have not visited all the nodes
    #   * The first condition is to support unconnected graphs. Because an unconnected graph never will enqueue nodes of the subgraphs disconnected and for that reason the
    #      condition of visited.Count < graph.Count never will be true
    #   * The second condition is a optimization to avoid to visit nodes already visited. For example, in Graph3, the edge A->B has a cost 9 will be enqueued
    #       first with a cost 9, but when we visit the node B, we will enqueue again the node A with a cost 5. So, that why we can avoid to visit nodes already visited with
    #       lower cost improving the number of iterations
    while len(queue) > 0 and len(distances) < len(graph):
        currentCost, currentNode = heapq.heappop(queue)

        # Ignore nodes already visited
        if currentNode  in visited:
            continue

        # Add the node to the visited nodes
        visited.add(currentNode)

        # Iterate over the neighbors of the current node
        for neighbor, neighborCost in graph[currentNode].items():
            neighborCumulativeCost = currentCost + neighborCost

            # Update the distance if the new cost is lower than the previous cost
            if neighborCumulativeCost < distances[neighbor]:
                distances[neighbor] = neighborCumulativeCost

                # Enqueue the neighbor in the queue, to understant what is the next node to be visited
                heapq.heappush(queue, (neighborCumulativeCost, neighbor))

    return distances


def dijkistra2(graph, source):
    distances = {}
    queue = [(0, source, source)]

    while len(queue) > 0 and len(distances) < len(graph):
        currentCost, currentNode, prev = heapq.heappop(queue)

        if currentNode in distances:
            continue

        distances[currentNode] = (currentCost, prev)

        for neighbor, neighborCost in graph[currentNode].items():
            neighborCumulativeCost = currentCost + neighborCost
            heapq.heappush(queue, (neighborCumulativeCost, neighbor, currentNode))

    return distances


# graph1.md
graph1 = {
    'A': {'B': 5, 'C': 1},
    'B': {'C': 4, 'D': 2, 'E': 4},
    'C': {'E': 5, 'B': 2, 'D': 5},
    'D': {'E': 2},
    'E': {}
}

# graph2.md
graph2 = {
    'A': {'B': 3, 'D': 4, 'S': 7},
    'B': {'A': 3, 'D': 4, 'S': 2, 'H': 1},
    'C': {'S': 3, 'L': 2},
    'D': {'A': 4, 'B': 4, 'F': 5},
    'E': {'G': 2, 'K': 5},
    'F': {'D': 5, 'H': 3},
    'G': {'E': 2, 'H': 2},
    'H': {'B': 1, 'F': 3, 'G': 2},
    'I': {'J': 6, 'K': 4, 'L': 4},
    'J': {'I': 6, 'K': 4, 'L': 4},
    'K': {'E': 5, 'I': 4, 'J': 4},
    'L': {'C': 2, 'I': 4, 'J': 4},
    'S': {'A': 7, 'B': 2, 'C': 3}
}

# graph3.md
graph3 = {
    'A': {'B': 9, 'C': 1},
    'B': {'C': 4, 'D': 2, 'E': 4},
    'C': {'E': 5, 'B': 2, 'D': 5},
    'D': {'E': 2},
    'E': {},
    'F': {'G': 4}
}


graph = graph3
origen = 'A'

for node, distance in dijkistra2(graph, origen).items():
    print(f'{origen} -> {node} ({distance})')