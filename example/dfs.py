#
# Implementation of the original DFS-algorithm
# DFS employs Stack data structure, none weighted
#

MAX = int(10**3)
INF = int(10**3)

import sys
sys.setrecursionlimit(INF)

from collections import deque

from bfs_algo import Path_iter, Path_recu


# Depth-first search
def DFS_iter(graph, sta):
    color[sta] = 0
    dist[sta]  = 0
    
    visit = deque()
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
        

if (__name__ == "__main__"):        
    # Initialisation for vertices and graph
    graph = [[] for i in range(MAX)]         # adjacency list           
    color = [-1 for i in range(MAX)]         # (-1, 0, 1) = (un, ing, full)
    path  = [-1 for i in range(MAX)]         # parent vertex
    dist  = [-1 for i in range(MAX)]         # time of first discovered
    full  = [-1 for i in range(MAX)]         # time of fully discovered 
        
    sta = 0
    fin = 4
        
    # Example
    graph_01 = [[1,3,8],[0,7],[3,5,7],[0,2,4],[3,8],[2,6],[5],[1,2],[0,4]]
    graph_02 = [[1,3],[0,2,3,5],[1,5],[0,1,4,5],[3],[1,2,3]]
    graph_03 = [[1,2,4],[3],[5],[2,5],[4],[]]
    graph    = graph_01
    
    DFS_iter(graph, sta)
    Path_iter(path, sta, fin)
    print()
    # print(dist[:fin+1])
    
    color = [-1 for i in range(MAX)]         
    path  = [-1 for i in range(MAX)]         
    dist  = [-1 for i in range(MAX)]   
    full  = [-1 for i in range(MAX)]       
    
    DFS_recu(graph, sta, -1)
    Path_recu(path, sta, fin)
    print()
    # print(dist[:fin+1])
    # print(full[:fin+1])


 