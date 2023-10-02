# Algorithms and Data Structures - Dijkstra

- [Description](#description)
- [Pseudocode](#pseudocode)
- [Demos](#demos)
  - [Graphs used in the demos](#graphs-used-in-the-demos)
  - [Implementation](#implementation)
    - [`diagram.py`](#diagrampy)
- [References](#references)
- [Contributions](#contributions)



## Description

The Dijkstra Algorithm falls under the category of "Shortest Path" problems in graphs. This is a classic optimization problem in graph theory, where the goal is to find the lowest weight path between two vertices in a weighted graph. The Dijkstra algorithm is particularly efficient for graphs with non-negative weights on the edges. Solving shortest path problems is crucial in various areas, such as computer networks, route planning, and logistics.



## Pseudocode

**Initialization:**

1. Select a source vertex;
2. Create a HashTable to store the vertices that have already been visited;
3. Create a dictionary to store the distances from the source to each vertex, initializing the distance from the source to itself as 0;
4. Create a Min-heap queue and add the source vertex with distance 0;

**Processing:**

5. While the queue is not empty and the number of visited vertices is less than the number of vertices in the graph:
   1. Retrieve the vertex with the smallest accumulated distance from the queue;
   2. If we are looking for the shortest path to a specific vertex, at this step, we can check if the current vertex is the destination vertex and terminate the neighbor processing loop;
   3. If the current vertex has already been visited, skip to the next vertex and go back to step 5.1;
   4. Add the current vertex to the HashTable of visited vertices;
   5. For each neighbor of the current vertex in the graph:
      1. Calculate the accumulated distance to the current vertex + the distance from the current vertex to the neighbor;
      2. If the neighbor is not in the distance dictionary or the accumulated distance is less than the neighbor's distance in the dictionary:
         1. Update the neighbor's distance in the dictionary;
         2. Add the neighbor to the queue with the accumulated distance to enter the priority queue;

**Finalization:**

6. If we are looking for the shortest path to a specific vertex, we can terminate when the destination vertex is found;
   1. Then, we traverse the dictionary from the destination to the source to obtain the shortest path;
7. If we are looking for the shortest path to all vertices, we can terminate when the queue is empty or all vertices have been visited;
   1. Then, we can return the distance dictionary.



## Demos

### Graphs used in the demos

* [Directed Graph (Digraph)](graph1.md)
* [Undirected Graph](graph2.md)
* [Disconnected Graph](graph3.md)

### Implementation

#### `diagram.py`
To run this demo, you need to install the following packages:

```bash
pip install networkx
pip install matplotlib
```



## References

* [usfca.edu](https://www.cs.usfca.edu/~galles/visualization/Dijkstra.html)
* [Pseudocode diagram](https://whimsical.com/djikstra-ULBhe3Sp9aVMKBzBiNNQLN)
* [Java implementation](https://github.com/giovannymassuia/algorithms/tree/main/dijkstra)



## Contributions

* [@giovannymassuia](https://github.com/giovannymassuia)
* [@wilsonneto-dev](https://github.com/wilsonneto-dev)
* [@Matheus](https://www.linkedin.com/in/matheus-silva-santos-90383234/)
