---
header-includes:
  - \usepackage[ruled,vlined,linesnumbered]{algorithm2e}
---

# Elementary algorithms

## Breadth-first search \(BFS\) algorithm

### Briefing
[Breadth-first search](https://en.wikipedia.org/wiki/Breadth-first_search) \(BFS\) belongs to a group of algorithms for traversing or searching tree or graph data structures; BFS traverse a connected component of a given graph and defines a spanning tree. Breadth-first search is an effective way to find all the vertices reachable from the a given source vertex. It starts at the tree root (or some arbitrary node of a graph, sometimes referred to as a _search key_\), and explores all of the neighbor nodes at the present depth prior to moving on to the nodes at the next depth level.


Breadth-first search can be used to solve many problems in graph theory, for example:
- Solving a maze;
- Finding the shortest path between two nodes $$u$$ and $$v$$, with path length measured by number of edges (an advantage over depth-first search);
- Computing the maximum flow in a flow network;
- Partitioning of the vertices into subsets that have the same distance from a given root vertex.


### Algorithm and Implementation
Intuitively, the basic idea of the breath-first search is this: send a wave out from source, $$sta$$; the wave hits all vertices at one-depth level from $$sta$$; from there, the wave hits all vertices at two-depth level from $$sta$$; etc. A FIFO queue **visit** is employed to maintain the wavefront: $$v$$ is in **visit** if and only if wave has hit $$v$$ but has not come out of $$v$$ yet.


To keep track of progress, breadth-first-search colors each vertex. Each vertex of the graph has one of three states, and, correspondingly, the state of a vertex, $$u$$, is stored in a _color_ variable as follows:
- **color**[$$u$$] = 0 or white - for the _undiscovered_ state,
- **color**[$$u$$] = 1 or gray - for the _discovered but not fully explored_ state, and
- **color**[$$u$$] = 2 or black - for the _fully explored_ state.


The **BFS(graph,** _sta_ **)** algorithm develops a breadth-first search tree with the source vertex, $$sta$$, as its root. The parent or predecessor of any other vertex in the tree is the vertex from which it was first discovered. For each vertex, $$v$$, the parent of $$v$$ is placed in the variable **path**[$$v$$]. Another variable, **dist**[$$v$$], computed by BFS contains the number of tree edges on the path from $$sta$$ to $$v$$. The breadth-first search uses a FIFO queue, **visit**, to store gray vertices. 

**Reserve for an image**

BFS builds a tree called a breadth-first-tree containing all vertices reachable from _sta_. The set of edges in the tree (called tree edges) contain \(**path**[_fin_], _fin_\) for all $$fin$$ where **path**[_fin_] $$\neq$$ _None_. If _fin_ is reachable from _sta_ then there is a unique path of tree edges from $$sta$$ to _fin_. 

**Reserve for an image**

Complexity of the BFS algorithm can be analysed as follows:
- The while-loop in BFS is executed at most V times; the reason is that every vertex is enqueued at most once. So, we have $$O(V)$$. 
- The for-loop inside the while-loop is executed at most E times if **G** is a directed graph or 2E times if **G** is undirected; the reason is that every vertex is dequeued at most once and we examine \($$u$$, $$v$$\) only when $$u$$ is dequeued. Therefore, every edge examined at most once if directed, at most twice if undirected. So, we have $$O(E)$$.
- Consequently, the total running time for breadth-first search traversal is $$O(V+E)$$.
- **Path\_finder(V,** _sta_ **,** _fin_ **)** has the complexity of $$O(V)$$.


### Implementation
Naive implementation of BFS in Python can be done as follows:

- Breadth-first search algorithm
    ```python
    from collections import deque
    
    def BFS(graph, sta):
        color[sta] = 0
        dist[sta]  = 0
        	
        visit = deque()
        visit.append(sta)
        
        while (len(visit) > 0):
            vh = visit.popleft()
            
            for vn in graph[vh]:
                if (color[vn] == -1):
                    color[vn] = 0
                    path[vn]  = vh
                    dist[vn]  = dist[vh]+1
                    
                    visit.append(vn)
            color[vh] = 1
    ```

- Path finding ITERATIVE-version
  ```python
  def Path_finder_iter(path, sta, fin):
      road = []
      
      if (fin == sta):
          print(sta)
          return
      
      if (path[fin] == -1):
          print('No path')
          return
      
      while True:
          road.append(fin)
          fin = path[fin]
          if (fin == sta):
              road.append(sta)
              break
          
      for i in range(len(road)-1, -1, -1):
          print(road[i], end = ' ')
  ```

- Path finding RECURSIVE-version
  ```python
  def Path_finder_recu(path, sta, fin):
  	if (fin == sta):
  		print(fin, end = ' ')
  	elif (path[fin] == -1):
  		print('No path')
  	else:
  		Path_recu(path, sta, path[fin])
  		print(fin, end = ' ')
  ```

- Example
  ```python
  # Initialisation for vertices and graph
  color = [-1 for i in range(MAX)]         # (-1, 0, 1) = (un, ing, full)
  path  = [-1 for i in range(MAX)]         # parent vertex
  dist  = [-1 for i in range(MAX)]         # distance from source
  graph = [[] for i in range(MAX)]         # adjacency list
  
  sta, fin = 0, 6
  	
  # Example
  graph_01 = [[1,3,8],[0,7],[3,5,7],[0,2,4],[3,8],[2,6],[5],[1,2],[0,4]]
  graph_02 = [[1,3],[0,2,3,5],[1,5],[0,1,4,5],[3],[1,2,3]]
  graph_03 = [[1,2,4],[3],[5],[2,5],[4],[]]
  
  graph = graph_01
  BFS(graph, sta)
  Path_finder_iter(path, sta, fin)   # 0 -> 3 -> 2 -> 5 -> 6
  Path_finder_recu(path, sta, fin)   # 0 -> 3 -> 2 -> 5 -> 6
  ```

Further notes (fine-tuning later):
- collections.deque is an alternative implementation of unbounded queues with fast atomic append() and popleft() operations that do not require locking;
- if you have multiple threads and you want them to be able to communicate without the need for locks, you're looking for Queue.Queue; if you just want a queue or a double-ended queue as a datastructure, use collections.deque.


### Problems for practice
The following problems from different sources can be used to practice the BFS algorithm:
- [hr Shortest reach](https://www.hackerrank.com/challenges/bfsshortreach/problem)
- [he Key generation](https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/)
- [spoj Validate the maze](https://www.spoj.com/problems/MAKEMAZE/)
- [lightoj Guilty prince](https://vjudge.net/problem/LightOJ-1012)
- [spoj Slick](https://www.spoj.com/problems/UCV2013H/)
- [cf C0580 Kefa and park](https://codeforces.com/problemset/problem/580/C)


## Depth-first search \(DFS\) algorithm
### Briefing
Depth-first search \(DFS\) is an algorithm for traversing or searching tree or graph data structures. Like breadth-first search, DFS traverse a connected component of a given graph and defines a spanning tree. The algorithm starts at the root node \(selecting some arbitrary node as the root node in the case of a graph\) and explores as far as possible along each branch before backtracking.


### Algorithm
The strategy followed by depth-first search is, as its name implies, to search _deeper_ in the graph whenever possible. Depth-first search selects a source vertex $u$, then traverses the graph by considering an arbitrary edge $$\(u, v\)$$ from the current vertex $u$. If the edge $$\(u, v\)$$ leads to a visited vertex $$v$$, then backs down to the vertex $$u$$. On the other hand, if edge $$\(u, v\)$$ leads us to an unvisited vertex, then paints the vertex $$v$$ and make it our current vertex, and repeat the above computation. Sooner or later, we will get to a _dead end_, meaning all the edges from our current vertex $$u$$ takes us to painted vertices. Because of this strategy, a LIFO stack **visit** is employed to maintain the focus on deepening the path. 

Similar to BFS, DFS also colors each vertex to keep track of progress by a _color_ variable, **colo**. DFS time-stams each vertex when its color is changed; when it is visited for the first time - white to gray - the time is recorded in **dist**, whereas, when it is fully discovered - gray to black - the time is recorded in **full** \(this operation is more conveniently performed in an recursive approach\). The path from one vertex to others can also be traced back through **path**. 

**Reserve for an image**

It can be seen that the DFS algorithm \(iterative-version\) is almost identical to that of BFS, except that the STACK structure is employed instead of the QUEUE one in order to maintain the deepening priority. There are two approach to implement DFS, iterative and recursive, and one should better familiarise with both methods to solve different types of problems. The problems in the next section will illustrate the usefulness of both methods. Lastly, the path along two connected vertices can also be traced back with **Path\_finder(V,** _sta_ **,** _fin_ **)**.  


### Implementation
Naive implementation of DFS in Python can be done as follows:
- Depth-first search algorithm, ITERATIVE-version
\inputpython{example/dfs_algo.py}{14}{30}
  ```python
  def DFS_iter(graph, sta):
      color[sta] = 0
      dist[sta]  = 0
      
      visit = collections.deque()
      visit.append(sta)
      
      while (len(visit) > 0):
          vh = visit.pop()
          
          for vn in graph[vh]:
              if (color[vn] == -1):
                  color[vn] = 0
                  path[vn]  = vh
                  dist[vn]  = dist[vh]+1
                  
                  visit.append(vn)
          color[vh] = 1
  ```

- Depth-first search algorithm, RECURSIVE-version
  ```python
  def DFS_recu(graph, vh, time):
      color[vh] = 0
      time     += 1
      dist[vh]  = time
          
      for vn in graph[vh]:
          if (color[vn] == -1):
              path[vn] = vh
              DFS_recu(graph, vn, time)
              
      color[vh] = 1
      time     += 1
      full[vh]  = time
  ```

- Example
  ```python
  # Initialisation for vertices and graph
  graph = [[] for i in range(MAX)]         # adjacency list           
  color = [-1 for i in range(MAX)]         # (-1, 0, 1) = (un, ing, full)
  path  = [-1 for i in range(MAX)]         # parent vertex
  dist  = [-1 for i in range(MAX)]         # time of first discovered
  full  = [-1 for i in range(MAX)]         # time of fully discovered 
      
  sta = 0
  fin = 4
      
  # Example
  graph = [[1,3,8],[0,7],[3,5,7],[0,2,4],[3,8],[2,6],[5],[1,2],[0,4]]
  
  DFS_iter(graph, sta)
  Path_finder_iter(path, sta, fin)
  
  # Re-initialisation
  DFS_recu(graph, sta, -1)
  Path_finder_recu(path, sta, fin)
  ```

Noted: please redo this example by hand to fully understand the path of each implementation, you can see that the path found by the iterative method is different than that by the recursive method or that by the BFS algorithm. 


### Problems for practice
The following problems from different sources can be used to practice the DFS algorithm:
- [spoj The last shot](https://www.spoj.com/problems/LASTSHOT/)
- [spoj Prayatna](https://www.spoj.com/problems/CAM5/)
- [spoj Bishu and his girlfriend](https://www.hackerearth.com/practice/algorithms/graphs/depth-first-search/practice-problems/algorithm/bishu-and-his-girlfriend/)
- [cf Lakes in Berland](https://codeforces.com/problemset/problem/723/D) 
- [spoj ALL IZZ WELL](https://www.spoj.com/problems/ALLIZWEL/)
- [uri Dudu service maker](https://www.urionlinejudge.com.br/judge/en/problems/view/1610)


## Topological sort
Later :)


## Strongly-connected components
Later :)
