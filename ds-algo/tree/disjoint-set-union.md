# Disjoint Set Union

## Briefing
A [disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) data structure (also called a union–find data structure or merge–find set because of its two main operation) is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set.

Applications:

- has a key role in Kruskal's algorithm for finding the minimum spanning tree of a graph;
- keeps track of the connected components of an undirected graph;

An example of classifying loops of friends (middle and right) connected to each others based on pairs of relationship (left) can be illustrated on the following image.

![Example of a Disjoint Set Union](../../.gitbook/assets/dsu.png)



## Operations and implementations
