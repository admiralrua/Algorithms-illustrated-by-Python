#
# Implementation of the original DFS-algorithm
# DFS employs Binary-Heap data structure, none negative weighted
#

MAX = int(10**3)
INF = int(10**3)

import sys
sys.setrecursionlimit(INF)

from bfs_algo import Path_iter

from heapq import heappush, heappop

def Dijkstra(graph, sta):
    
    visit = []
    heappush(visit, (sta, 0))
    dist[sta] = 0
    
    while (len(visit) != 0):
        v_here = heappop(visit)
        
        ind = v_here[0]
        dis = v_here[1]
        
        for v_next in graph[ind]:
            ind_n = v_next[0]
            dis_n = v_next[1]
            
            if (dis + dis_n < dist[ind_n]):
                dist[ind_n] = dis + dis_n
                path[ind_n] = ind
                heappush(visit, (ind_n, dist[ind_n]))
        

if (__name__ == "__main__"):        
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
    Path_iter(path, sta, fin)          # 0 -> 1 -> 3 -> 2 -> 5 -> 4
 