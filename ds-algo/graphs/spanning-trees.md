# Minimum spanning trees
There are several well-known algorithms for finding [the minimum spanning tree](https://en.wikipedia.org/wiki/Minimum_spanning_tree) in a graph include Prim algorithm, Kruskal algorithm, Reverse-delete algorithm and Borůvka's algorithm. The most basic form of Prim's algorithm only finds minimum spanning trees in connected graphs; whereas the others find the minimum spanning forest in a possibly disconnected graph. However, running Prim's algorithm separately for each connected component of the graph, it can also be used to find the minimum spanning forest. In terms of their asymptotic time complexity, these three algorithms are equally fast for sparse graphs, but slower than other more sophisticated algorithms. However, for graphs that are sufficiently dense, Prim algorithm can be made to run in linear time, meeting or improving the time bounds for other algorithms.

## Prim algorithm
### Briefing
[Prim \(also known as Jarník\) algorithm](https://en.wikipedia.org/wiki/Prim's_algorithm) is a greedy algorithm that finds a minimum spanning tree for a weighted undirected graph. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. The algorithm operates by building this tree one vertex at a time, from an arbitrary starting vertex, at each step adding the cheapest possible connection from the tree to another vertex.

### Implementation
The Prim algorithm is quite straightfoward. Howver, the time complexity of the algorithm depends heavily on the data structures used for the graph and for odering the edges by weight. The following table shows the consequences of several typical choices:

| Minimum edge weight data structure | Time complexity (total)          |
| --- | --- |
| adjacency matrix, searching	       | $$O(V^2)$$                       |
| binary heap and adjacency list	   | $$O((V+E)\log V) = O(E \log V)$$ |
| Fibonacci heap and adjacency list	 | $$O(E + V \log V)$$              |

The implementation of Prim algorithm with the binary heap and the adjacency list can be done as follows:

```python
from heapq import heappush, heappop

INF = 10**9

def prims(sta):
	visit     = []
	dist[sta] = 0
	heappush(visit, (0, sta))
	
	while (len(visit) > 0):
		vh_data     = heappop(visit)
		vh          = vh_data[1]
		visited[vh] = True
		
		for vn_data in graph[vh]:
			vn = vn_data[0]
			w  = vn_data[1]
			
			if (visited[vn] == False) and (w < dist[vn]):
				dist[vn] = w
				path[vn] = vh
				heappush(visit, (w, vn))
```

To print out the tree and its corresponding minimum weight, we can do as follows:

```python				
def mst_out():
	ans = 0
	
	for i in range(n+1):
		if (path[i] == -1):
			continue
		ans += dist[i]
		
		# print("{0} - {1}: {2}".format(path[i], i, dist[i]))
		
	print("Weight of the MSTL {0}".format(ans))
```

Here is an example of using Prim algorithm:

```python
n = 4

graph   = [[]    for i in range(n+1)]
dist    = [INF   for i in range(n+1)] 
path    = [-1    for i in range(n+1)] 
visited = [False for i in range(n+1)] 

graph = [[],[(2,10),(3,5),(4,7)],[(1,10),(3,15),(4,2)],[(1,5),(2,15),(4,40)],[(1,7),(2,2),(3,40)]]
	
prims(1)
mst_out()
```

### Problem for practice
Later :)


## Kruskal algorithm
[Kruskal algorithm](https://en.wikipedia.org/wiki/Kruskal\'s_algorithm) is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that connects any two trees in the forest. It is a greedy algorithm in graph theory as it finds a minimum spanning tree for a connected weighted graph adding increasing cost arcs at each step. This means it finds a subset of the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is minimized. If the graph is not connected, then it finds a minimum spanning forest (a minimum spanning tree for each connected component).

### Implementation
Later :)

### Problem for practice
Later :)


## Reverse-delete algorithm
[Reverse-delete algorithm](https://en.wikipedia.org/wiki/Reverse-delete_algorithm) is an algorithm in graph theory used to obtain a minimum spanning tree from a given connected, edge-weighted graph. It first appeared in Kruskal (1956), but it should not be confused with Kruskal's algorithm which appears in the same paper. If the graph is disconnected, this algorithm will find a minimum spanning tree for each disconnected part of the graph. The set of these minimum spanning trees is called a minimum spanning forest, which contains every vertex in the graph.

This algorithm is a greedy algorithm, choosing the best choice given any situation. It is the reverse of Kruskal's algorithm, which is another greedy algorithm to find a minimum spanning tree. Kruskal’s algorithm starts with an empty graph and adds edges while the Reverse-Delete algorithm starts with the original graph and deletes edges from it. 

### Implementation
Later :)

### Problem for practice
Later :)


## Borůvka algorithm
[Bor\ůvka algorithm](https://en.wikipedia.org/wiki/Borůvka's_algorithm) is a greedy algorithm for finding a minimum spanning tree in a graph for which all edge weights are distinct, or a minimum spanning forest in the case of a graph that is not connected.

### Implementation
Later :)

### Problem for practice
Later :)
