using static System.Console;
using Graph = System.Collections.Generic.Dictionary<char, System.Collections.Generic.Dictionary<char, int>>;


// var graph = new Graph
// {
//     ['A'] = new() { ['B'] = 3, ['D'] = 4, ['S'] = 7 },
//     ['B'] = new() { ['A'] = 3, ['D'] = 4, ['S'] = 2, ['H'] = 1 },
//     ['C'] = new() { ['S'] = 3, ['L'] = 2 },
//     ['D'] = new() { ['A'] = 4, ['B'] = 4, ['F'] = 5 },
//     ['E'] = new() { ['G'] = 2, ['K'] = 5 },
//     ['F'] = new() { ['D'] = 5, ['H'] = 3 },
//     ['G'] = new() { ['E'] = 2, ['H'] = 2 },
//     ['H'] = new() { ['B'] = 1, ['F'] = 3, ['G'] = 2 },
//     ['I'] = new() { ['J'] = 6, ['K'] = 4, ['L'] = 4 },
//     ['J'] = new() { ['I'] = 6, ['K'] = 4, ['L'] = 4 },
//     ['K'] = new() { ['E'] = 5 ,['I'] = 4, ['J'] = 4 },
//     ['L'] = new() { ['C'] = 2, ['I'] = 4, ['J'] = 4 },
//     ['S'] = new() { ['A'] = 7, ['B'] = 2, ['C'] = 3 }
// };
var graph = new Graph
{
    ['A'] = new() { ['B'] = 5, ['C'] = 1 },
    ['B'] = new() { ['D'] = 2, ['B'] = 4, ['E'] = 4 },
    ['C'] = new() { ['E'] = 5, ['B'] = 2, ['D'] = 5 },
    ['D'] = new() { ['E'] = 2 },
    ['E'] = new()
};

var origen = 'A';
var result = Dijkstra(graph, origen);

foreach (var (key, value) in result)
{
    WriteLine($"{origen} -> {key} ({value})");
}



static Dictionary<char, int> Dijkstra(Graph graph, char origen)
{
    var visited = new HashSet<char>();
    var distances = new Dictionary<char, int>(graph.Count);

    var queue = new PriorityQueue<(char, int), int>();
    queue.Enqueue((origen, 0), 0);

    while (visited.Count < graph.Count)
    {
        var (current, cost) = queue.Dequeue();

        if (visited.Contains(current))
        {
            continue;
        }

        visited.Add(current);


        foreach (var (neighbour, neighbourCost) in graph[current])
        {
            var neighborCumulativeCost = cost + neighbourCost;

            if (!distances.ContainsKey(neighbour) ||
                neighborCumulativeCost < distances[neighbour])
            {
                distances[neighbour] = neighborCumulativeCost;
                queue.Enqueue((neighbour, neighborCumulativeCost), neighborCumulativeCost);
            }
        }
    }

    return distances;
}
