#
# Implementation of the original Roy-Floyd-Warshall algorithm 
# none negative-weight cycle
# adjacency matrix
#

MAX = int(10**3)
INF = int(10**9)


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
        
            
def rfw_Path_finder(sta, fin):
    prev = []
    
    while (sta != fin):
        prev.append(fin)
        fin = path[sta][fin]
        
    prev.append(sta)
    
    for i in range(len(prev)-1,-1,-1):
        print(prev[i], end = ' ' if i > 0 else '\n')
        

if __name__ == '__main__':
    n = 6
   
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

                    