# MST
# https://www.spoj.com/problems/MST/
# AC

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

                
def mst_out():
    ans = 0
    
    for i in range(n+1):
        if (path[i] == -1):
            continue
        ans += dist[i]
        
        # print("{0} - {1}: {2}".format(path[i], i, dist[i]))
        
    # print("Weight of the MSTL {0}".format(ans))
    print(ans)
    

if __name__ == '__main__':
    # import sys
    # sys.stdin = open('INP.txt', 'r')
    
    n, m = map(int, input().split())
    
    graph   = [[]    for i in range(n+1)]
    dist    = [INF   for i in range(n+1)] 
    path    = [-1    for i in range(n+1)] 
    visited = [False for i in range(n+1)] 
    
    for i in range(m):
        u, v, w = map(int, input().split())
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    # graph = [[],[(2,10),(3,5),(4,7)],[(1,10),(3,15),(4,2)],[(1,5),(2,15),(4,40)],[(1,7),(2,2),(3,40)]]
    
    prims(1)
    mst_out()
        
"""
4 6
1 2 10
1 3 5
1 4 7
2 4 2
2 3 15
3 4 40
"""    