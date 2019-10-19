#
# Implementation of the original BFS-algorithm
# BFS employs Queue data structure, none weighted
#

MAX = int(10**4)
INF = int(10**5)

import sys
sys.setrecursionlimit(INF)

from collections import deque

# Breadth-first search
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
		
		
# Path finding ITERATION
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
		
		
# Path finding RECURSION
def Path_recu(path, sta, fin):
	if (fin == sta):
		print(fin, end = ' ')
	elif (path[fin] == -1):
		print('No path')
	else:
		Path_recu(path, sta, path[fin])
		print(fin, end = ' ')
			
		
if (__name__ == "__main__"):
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


 