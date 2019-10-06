# Shortest paths

## Dijkstra algorithm \(single-source\)
### Briefing
[Dijkstra algorithm](https://en.wikipedia.org/wiki/Dijkstra\'s\_algorithm) is an algorithm to find the shortest paths from one nodes to all other nodes in a graph with non-negative weights.


### Algorithm
Dijkstra algorithm uses a greedy strategy in the sense that it always choose the _lightest_ or _closest_ vertex. Algorithm starts at the source vertex, $$s$$, it grows a tree, **T**, that ultimately spans all vertices reachable from $$s$$. Vertices are added to **T** in order of distance i.e., first $$s$$, then the vertex closest to $$s$$, then the next closest, and so on. Greedy strategies do not always yield optimal results in general but Dijkstra algorithm does indeed compute shortest paths. With the graph having weighted edges, Dijkstra algorithm can compute the path with the minimum **cost**.

The general implementation has the complexity of $$O(V^2)$$. However, if the priority queue or the binary heap is employed, the complexity reduces to $$O(E \log V)$$


**Reserve for an image**

The path from one vertex to all other vertices (if they are connected) can be traced back with **Path\_finder(V,** _sta_ **,** _fin_ **)** based on the **path** array; similarly, the cost can be taken directly from the **dist** array.


### Implementation
Naive implementation of Dijkstra algorithm in Python can be done as follows:

- Dijkstra's algorithm
  ```python
  from heapq import heappush, heappop
  
  def Dijkstra(graph, sta):
      
      visit = []
      heappush(visit, (sta, 0))
      dist[sta] = 0
      
      while (len(visit) != 0):
          v_here = heappop(visit)
          
          ind = v_here[1]
          dis = v_here[0]
          
          for v_next in graph[ind]:
              ind_n = v_next[0]
              dis_n = v_next[1]
              
              if (dis + dis_n < dist[ind_n]):
                  dist[ind_n] = dis + dis_n
                  path[ind_n] = ind
                  heappush(visit, (dist[ind_n], ind_n))
  ```

- Example
  ```python
  # Initialisation for vertices and graph
  graph = [[]  for i in range(MAX)]         # adjacency list      
  path  = [-1  for i in range(MAX)]         # parent vertex
  dist  = [INF for i in range(MAX)]         # distance from source      
      
  sta, fin = 0, 4
      
  # Example
  # graph[i].append((j, k)) --> vertex i to vertex j, cost = 5
  graph = [[(1,1)],[(2,5),(3,2),(5,7)],[(5,1)],
           [(0,2),(2,1),(4,4)],[(3,3)],[(4,1)]]
  
  visit = Dijkstra(graph, sta)
  print(dist[fin])                   # 6
  Path_finder_iter(path, sta, fin)   # 0 -> 1 -> 3 -> 2 -> 5 -> 4
  ```


### Problems for practice
The following problems from different sources can be used to practice the Dijkstra algorithm:
- [lightoj Commandos](https://vjudge.net/problem/LightOJ-1174)
- [spoj Travelling cost](https://www.spoj.com/problems/TRVCOST/)
- [spoj The shortest path](https://www.spoj.com/problems/SHPATH/)
- [spoj Mice and maze](https://www.spoj.com/problems/MICEMAZE/) 
- [spoj Traffic network](https://www.spoj.com/problems/TRAFFICN/) 
- [uva Sending email](https://uva.onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1927)
- Not yet solved problems:
  - [cf Complete the graph](https://codeforces.com/contest/715/problem/B)
  - [cf Jzzhu and cities](https://codeforces.com/contest/449/problem/B)
  - [cf E Shortest path](https://codeforces.com/contest/59/problem/E)
  - [cf E The classic problem](https://codeforces.com/contest/464/problem/E)
  - [cf E President and roads](https://codeforces.com/contest/567/problem/E)
  - [cf K Police catching thief](https://codeforces.com/problemset/gymProblem/100589/K)
  - [he Synchronous shopping](https://www.hackerrank.com/challenges/synchronous-shopping/problem)
  - [spoj Almost Shortest Path](https://www.spoj.com/problems/SAMER08A/)
  - [spoj](https://www.spoj.com/problems/tag/dijkstra-s-algorithm)


## Bellman-Ford-Moore algorithm \(single-source\)
### Briefing
[Bellman–Ford–Moore algorithm](https://en.wikipedia.org/wiki/Bellman-Ford_algorithm) is an algorithm to find the shortest paths from one nodes to all other nodes in a graph with non-negative cycle. [Another good writting about BFM algorithm](https://www.programiz.com/dsa/bellman-ford-algorithm).


### Algorithm
Bellman–Ford–Moore algorithm ...


**Reserve for an image**


### Implementation
Naive implementation of Bellman–Ford–Moore algorithm in Python can be done as follows:
- Bellman–Ford–Moore algorithm
  ```python
  def bfm_algo(graph, dist, sta):
      
      dist[sta] = 0
      
      # the first n-1 loops are for ptimising the cost
      # the last n-th loop is for detecting a negative-weight cycle
      for i in range(n):
          for j in range(m):
              u, v, w = graph[j]
              
              if ((dist[u] != INF) and (dist[u] + w < dist[v])):
                  dist[v] = dist[u] + w
                  path[v] = u
                  
                  if (i == n-1):
                      return True        # Negative-weight cycle
                  
      return False
  ```

- Example
  ```python
  n, m  = 6, 10
  graph = []
  path  = [-1  for i in range(n)]
  dist  = [INF for i in range(n)]
  
  # Example
  # graph.append((i, j, k)) --> vertex i to vertex j, cost k
  graph = [(0,1,1),(1,2,5),(1,3,-2),(1,5,7),(2,5,-1),
           (3,0,2),(3,2,-1),(3,4,4),(4,3,3),(5,4,1)]
  
  sta, fin = 0, 4
  nwc = bfm_algo(graph, dist, sta)
  print('Has a NWC.' if nwc else 'Doesnt have NWC.')     # Doesnt have NWC.
  print(dist[fin])                   # -2
  Path_iter(path, sta, fin)          # 0 -> 1 -> 3 -> 2 -> 5 -> 4
  ```


### Problems for practice
The following problems from different sources can be used to practice the Bellman–Ford–Moore algorithm:
- [a](b)


## Roy-Floyd-Warshall algorithm \(all-pairs\)
### Briefing
[Roy-Floyd–Warshall algorithm](https://en.wikipedia.org/wiki/Floyd-Warshall_algorithm) is an algorithm for finding shortest paths in a weighted graph with positive or negative edge weights \(but with no negative cycles\). A single execution of the algorithm will find the lengths \(summed weights\) of shortest paths between all pairs of vertices.


### Algorithm
Roy-Floyd-Warshall algorithm ...

**Reserve for an image**


### Implementation
Naive implementation of Roy-Floyd-Warshall algorithm in Python can be done as follows:
- Roy-Floyd-Warshall algorithm
  ```python
  def rfw_algo(graph, dist):
      # Initialisation
      for i in range(n):
          for j in range(n):
              dist[i][j] = graph[i][j]
              
              if (graph[i][j] != INF) and (i != j):
                  path[i][j] = i
              else:
                  path[i][j] = -1
  	
      # Optimisation
      for k in range(n):
          for i in range(n):
              for j in range(n):
                  if dist[i][j] > dist[i][k] + dist[k][j]:
                      dist[i][j] = dist[i][k] + dist[k][j]
                      path[i][j] = path[k][j]
      
      # Negative-cycle detect
      for i in range(n):
          if (dist[i][i] < 0):
              return True
          
      return False
  ```

- Path-finding
  ```python
  def rfw_Path_finder(sta, fin):
      prev = []
      
      while (sta != fin):
          prev.append(fin)
          fin = path[sta][fin]
          
      prev.append(sta)
      
      for i in range(len(prev)-1,-1,-1):
          print(prev[i], end = ' ' if i > 0 else '\n')
  ```

- Example
  ```python
  n     = 6  
  graph = [[None for i in range(n)] for j in range(n)]
  dist  = [[None for i in range(n)] for j in range(n)]
  path  = [[None for i in range(n)] for j in range(n)]
  
  # Example
  graph = [[  0,  1,INF,INF,INF,INF],
           [INF,  0,  5, -2,INF,  7],
           [INF,INF,  0,INF,INF, -1],
           [  2,INF, -1,  0,  4,INF],
           [INF,INF,INF,  3,  0,INF],
           [INF,INF,INF,INF,  1,  0]]
  
  nwc = rfw_algo(graph, dist)
  print('Has a NWC.' if nwc else 'Doesnt have NWC.')     # Doesnt have NWC.
  
  sta, fin = 4, 0
  print(dist[sta][fin])              # 5
  rfw_Path_finder(sta, fin)          # 4 -> 3 -> 0
      
  sta, fin = 0, 4
  print(dist[sta][fin])              # -2
  rfw_Path_finder(sta, fin)          # 0 -> 1 -> 3 -> 2 -> 5 -> 4 
  ```


### Problems for practice
The following problems from different sources can be used to practice the Roy-Floyd-Warshall algorithm:
- [a](b)


## Johnson algorithm \(all-pairs\)
Later :)


