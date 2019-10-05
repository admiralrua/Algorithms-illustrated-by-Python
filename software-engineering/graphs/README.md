# Graphs

## Introduction
[Graph theory](https://en.wikipedia.org/wiki/Graph_theory) is an area of mathematics that deals with, at least, the following types of problems:

- connection, 
- scheduling, 
- transportation, 
- network analysis,
- games and Puzzles. 

The graph theory has important applications in Critical path analysis, Social psychology, Matrix theory, Set theory, Topology, Group theory, Molecular chemistry, and Searching.

A [graph](https://en.wikipedia.org/wiki/Graph_(abstract_data_type)) data structure consists of a finite set of **vertices** (**V**, also called nodes or points), together with a set of unordered pairs of these vertices for an undirected graph or a set of ordered pairs for a directed graph. These pairs are known as **edges** (**E**, also called links or lines), and for a directed graph are also known as arrows. A graph data structure may also associate to each edge some value, such as a symbolic label or a numeric attribute (cost, capacity, length, etc.).

There are several ways to classify a graph being named as:
- Based on simplicity:
  - **Simple graph**: there is only one or no connection between every two vertices;
  - **Non-simple graph**: there may be more than one connection between two vertices;
  - **Graph with loops**: there may be an edge with the identical begin and end nodes.
- Based on direction:
  - **Undirected graph**: on any edge, we can go freely from one vertex to another;
  - **Directed graph**: on a certain edge, we can only go from one vertex to another.
- Based on edges' value:
  - **None weighted**: there is no value or an identical value for all edges;
  - **Weighted**: each edge may have different values representing the cost/length/.... 

Some other non-trivial definitions of a graph are presented here:
- **Degree**: a degree of a vertex is a number of edges associated to that vertex of a number of vertices connected to that vertex. For a directed graph, the out-degree is different from the in-degree.
- **Path**: a list of vertices $$v_{0}$$, $$v_{1}$$, $$v_{2}$$,... $$v_{n-1}$$, $$v_{n}$$ which represents a list of edges including exactly $$(v_{0}, v_{1})$$, $$(v_{1}, v_{2})$$,... $$(v_{n-1}, v_{n})$$. Then, it can be said that there is a path from $$v_{0}$$ to $$v_{n}$$.
- **Circuit**: a path in which $$v_{0}$$ = $$v_{n}$$.
- **Connected graph**: is a graph in which there is a path between any pair of two vertices $$u$$ and $$v$$.


Different data structures can be used to represent a graph as follows:
- **Adjacency matrix**: A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.
- **Edge list**: Edges are stored as a pair of begin and end vertices with or without the weight of that edge.
- **Adjacency list**: Vertices are stored as records or objects, and every vertex stores a list of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.
