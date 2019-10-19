#
# Implementation of the original Bellman–Ford–Moore algorithm 
# none negative-weight cycle
# edge list
#

MAX = int(10**3)
INF = int(10**9)

from bfs_algo import Path_iter

# Bellman–Ford–Moore algorithm        
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


if __name__ == "__main__": 
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
