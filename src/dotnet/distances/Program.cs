using static System.Console;
using Graph = System.Collections.Generic.Dictionary<char, System.Collections.Generic.Dictionary<char, int>>;

/* graph1.md */
var graph1 = new Graph
{
    ['A'] = new() { ['B'] = 5, ['C'] = 1 },
    ['B'] = new() { ['C'] = 4, ['D'] = 2, ['E'] = 4 },
    ['C'] = new() { ['E'] = 5, ['B'] = 2, ['D'] = 5 },
    ['D'] = new() { ['E'] = 2 },
    ['E'] = new()
};

/* graph2.md */
var graph2 = new Graph
{
    ['A'] = new() { ['B'] = 3, ['D'] = 4, ['S'] = 7 },
    ['B'] = new() { ['A'] = 3, ['D'] = 4, ['S'] = 2, ['H'] = 1 },
    ['C'] = new() { ['S'] = 3, ['L'] = 2 },
    ['D'] = new() { ['A'] = 4, ['B'] = 4, ['F'] = 5 },
    ['E'] = new() { ['G'] = 2, ['K'] = 5 },
    ['F'] = new() { ['D'] = 5, ['H'] = 3 },
    ['G'] = new() { ['E'] = 2, ['H'] = 2 },
    ['H'] = new() { ['B'] = 1, ['F'] = 3, ['G'] = 2 },
    ['I'] = new() { ['J'] = 6, ['K'] = 4, ['L'] = 4 },
    ['J'] = new() { ['I'] = 6, ['K'] = 4, ['L'] = 4 },
    ['K'] = new() { ['E'] = 5 ,['I'] = 4, ['J'] = 4 },
    ['L'] = new() { ['C'] = 2, ['I'] = 4, ['J'] = 4 },
    ['S'] = new() { ['A'] = 7, ['B'] = 2, ['C'] = 3 }
};

/* graph3.md */
var graph3 = new Graph
{
    ['A'] = new() { ['B'] = 9, ['C'] = 1 },
    ['B'] = new() { ['C'] = 4, ['D'] = 2, ['E'] = 4 },
    ['C'] = new() { ['E'] = 5, ['B'] = 2, ['D'] = 5 },
    ['D'] = new() { ['E'] = 2 },
    ['E'] = new(),
    ['F'] = new() { ['G'] = 4 },
};


var graph = graph3;
var origen = 'A';

foreach (var (node, distance) in Dijkstra(graph, origen))
{
    WriteLine($"{origen} -> {node} ({distance})");
}


static Dictionary<char, int> Dijkstra(Graph graph, char origin)
{
    // Structure to store the nodes already visited, we use a HashTable because has a O(1) complexity
    var visited = new HashSet<char>();

    // Structure to store the distances from the origin to each node, we use a Dictionary because has a O(1) complexity
    var distances = new Dictionary<char, int>(graph.Count);

    // Added the distance from the origin to itself
    distances[origin] = 0;

    // PriorityQueue is a min-heap, we use it to get the next node with the lowest cost. The min-heap has a O(log n) complexity
    //  <(char, int), int> -> (node, cost), cost
    var queue = new PriorityQueue<(char, int), int>();

    // Initialize the queue with the origin node. And the cost from the origin to itself is 0
    queue.Enqueue((origin, 0), 0);

    // While the queue is not empty and we have not visited all the nodes
    //   * The first condition is to support unconnected graphs. Because an unconnected graph never will enqueue nodes of the subgraphs disconnected and for that reason the
    //      condition of visited.Count < graph.Count never will be true
    //   * The second condition is a optimization to avoid to visit nodes already visited. For example, in Graph3, the edge A->B has a cost 9 will be enqueued
    //       first with a cost 9, but when we visit the node B, we will enqueue again the node A with a cost 5. So, that why we can avoid to visit nodes already visited with
    //       lower cost improving the number of iterations
    while (queue.Count > 0 && visited.Count < graph.Count)
    {
        var (currentNode, currentCost) = queue.Dequeue();
        if (visited.Contains(currentNode))
        { // Ignore nodes already visited
            continue;
        }

        // Add the node to the visited nodes
        visited.Add(currentNode);

        // Iterate over the neighbors of the current node
        foreach (var (neighbor, neighborCost) in graph[currentNode])
        {
            var neighborCumulativeCost = currentCost + neighborCost;

            // Add the neighbor in the distances dictionary if it was not added before or update it if the new cost is lower
            if (!distances.ContainsKey(neighbor) ||
                neighborCumulativeCost < distances[neighbor])
            {
                distances[neighbor] = neighborCumulativeCost;

                // Enqueue the neighbor in the queue (min heap), to understant what is the next node to be visited
                queue.Enqueue((neighbor, neighborCumulativeCost), neighborCumulativeCost);
            }
        }
    }

    return distances;
}
