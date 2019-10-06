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


### Algorithm
Intuitively, the basic idea of the breath-first search is this: send a wave out from source, $$sta$$; the wave hits all vertices at one-depth level from $$sta$$; from there, the wave hits all vertices at two-depth level from $$sta$$; etc. A FIFO queue **visit** is employed to maintain the wavefront: $$v$$ is in **visit** if and only if wave has hit $$v$$ but has not come out of $$v$$ yet.

To keep track of progress, breadth-first-search colors each vertex. Each vertex of the graph has one of three states, and, correspondingly, the state of a vertex, $$u$$, is stored in a _color_ variable as follows:
- **color**[$$u$$] = 0 or white - for the _undiscovered_ state,
- **color**[$$u$$] = 1 or gray - for the _discovered but not fully explored_ state, and
- **color**[$$u$$] = 2 or black - for the _fully explored_ state.

The **BFS(V, E, sta)** algorithm develops a breadth-first search tree with the source vertex, $$sta$$, as its root. The parent or predecessor of any other vertex in the tree is the vertex from which it was first discovered. For each vertex, $$v$$, the parent of $$v$$ is placed in the variable **path**[$$v$$]. Another variable, **dist**[$$v$$], computed by BFS contains the number of tree edges on the path from $$sta$$ to $$v$$. The breadth-first search uses a FIFO queue, **visit**, to store gray vertices.

```
\caption{\textbf{BFS(V, E, sta)} \label{bfs}}
\Begin{
   \tcc*[r]{initialisation, this can be done outside the function as well}
   \For{each $u$ in \textbf{V}}{
      \textbf{color}[$u$] = white  \\
      \textbf{dist}[$u$]  = INF    \\
      \textbf{path}[$u$]  = None   \\
   }
   \vspace{\baselineskip}
   
   \textbf{color}[$sta$] = gray                 \tcc*[r]{source vertext discovered} 
   \textbf{dist}[$sta$]  = 0                    \tcc*[r]{initialise} 
   \textbf{path}[$sta$]  = None                 \tcc*[r]{initialise} 
   \textbf{visit} $\rightarrow$ \{\}            \tcc*[r]{create an empty queue} 
   ENQUEUE(\textbf{visit}, $sta$)               \tcc*[r]{put a vertex in a queue} 
   \vspace{\baselineskip}
   
   \While{\textbf{visit} is not empty}{
      $u$ $\leftarrow$ DEQUEUE(\textbf{visit}) \\
      \For{each $v$ in adjacent to $u$}{
         \If{\textbf{color}[$v$] $\leftarrow$ white}{
            \textbf{color}[$v$] = gray                   \tcc*[r]{source vertext discovered} 
            \textbf{dist}[$v$]  = dist[$u$]+1            \tcc*[r]{initialise} 
            \textbf{path}[$v$]  = $u$                    \tcc*[r]{initialise} 
            ENQUEUE(\textbf{visit}, $v$)           
         }
      }
      \textbf{color}[$u$] = black     
   }   
}
```

BFS builds a tree called a breadth-first-tree containing all vertices reachable from $$sta$$. The set of edges in the tree (called tree edges) contain \(**path**[$$fin$$], $$fin$$\) for all $$fin$$ where path[$$fin$$] $$\neq$$ None. If $$fin$$ is reachable from $$sta$$ then there is a unique path of tree edges from $$sta$$ to $$fin$$. **Path\_finder(V, sta, fin)** prints the vertices along that path.

\begin{algorithm}[H]
\caption{**Path\_finder(V, sta, fin)} \label{bfs_path}}
\Begin{
   \uIf{$$fin$$ = $$sta$$}{
      print($$sta$$)
   }
   \uElseIf{**path}[$$fin$$] = None}{
      print(No path from $$sta$$ to $$fin$$)   
   }
   \Else{
      **BFS\_Path(V, sta, **path}[$$fin$$])} \\
      print $$fin$$
   }
}
\end{algorithm}

Complexity of the BFS algorithm can be analysed as follows:
- The while-loop in BFS is executed at most V times; the reason is that every vertex is enqueued at most once. So, we have $$O(V)$$. 
- The for-loop inside the while-loop is executed at most E times if **G** is a directed graph or 2E times if **G** is undirected; the reason is that every vertex is dequeued at most once and we examine \($$u$$, $$v$$\) only when $$u$$ is dequeued. Therefore, every edge examined at most once if directed, at most twice if undirected. So, we have $$O(E)$$.
- Consequently, the total running time for breadth-first search traversal is $$O(V+E)$$.
- **Path\_finder(V, sta, fin)** has the complexity of $$O(V)$$.


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
  def Path_iter(path, sta, fin):
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
  def Path_recu(path, sta, fin):
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
  Path_iter(path, sta, fin)   # 0 -> 3 -> 2 -> 5 -> 6
  Path_recu(path, sta, fin)   # 0 -> 3 -> 2 -> 5 -> 6
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



## Topological sort



## Strongly-connected components

