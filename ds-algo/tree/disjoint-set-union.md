# Disjoint Set Union

## Briefing
A [disjoint-set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) data structure (also called a union–find data structure or merge–find set because of its two main operation) is a data structure that tracks a set of elements partitioned into a number of disjoint (non-overlapping) subsets. It provides near-constant-time operations to add new sets, to merge existing sets, and to determine whether elements are in the same set.

Applications:

- has a key role in Kruskal's algorithm for finding the minimum spanning tree of a graph;
- keeps track of the connected components of an undirected graph;

An example of classifying loops of friends (middle and right) connected to each others based on pairs of relationship (left) can be illustrated on the following image.

![Example of a Disjoint Set Union](../../.gitbook/assets/dsu.png)


## Operations and implementations
A disjoint-set forest consists of a number of elements each of which stores an _identification number_, a _parent pointer_, and, in efficient algorithms, either a _size_ or a _rank_ value. Forests can be represented compactly in memory as arrays in which parents are indicated by their array index. A root of a disjoint-set forest is a vertex having the parent as itself.

There are two, actually three including the initialisation, operations of a disjoin-set: makeSet, findSet and unionSet.

### makeSet
** makeSet** makes a new set by creating a new element with a unique _id_, a _rank_ of 0, a _size_ of 1 and a parent pointer to itself.

The following code initialises a disjoint-set:

```python
def makeSet(size):
    global parent, ranks, sizes
    parent = [i for i in range(size + 1)]
    ranks  = [0 for i in range(size + 1)]
    sizes  = [1 for i in range(size + 1)]
```


### findSet
**findSet**\(_u_\) returns the representative (also called leader) of the set that contains the element _u_. This representative is an element of its corresponding set which is selected in each set by the data structure itself (and can change over time, namely after **unionSet** calls).

A naive implementation of **findSet**\(_u_\) simply climb the parent of the vertex _u_ until reaching the root. 

```python
def findSet(u):
    if (u != parent[u]):
        u = findSet(parent[u])       
    return u
```

However this implementation is inefficient, i.e. with trees degenerate into long chains, **findSet**\(_u_\) can take $$O(n)$$ time. 

The **findSet** operation can be optimised in the way that the path from \(_u_\) to _root_ is not incrementally shortened as in the naive implementation. There are three types of optimisation, namely:

- **path compression**: every node points to the root whenever **findSet** is used on it.
  ```python
  def findSet(u):
      if (u != parent[u]):
          parent[u] = findSet(parent[u])       
      return parent[u]
  ```
- **path halving**: every other node on the path points to its grandparent.
  ```python
  def findSet(u):
      while (u != parent[u]):
          parent[u] = parent[parent[u]]
          u = parent[u]      
      return u
  ```
- **path splitting**: every node on the path points to its grandparent.
  ```python
  def findSet(u):
      while (u != parent[u]):
          u, parent[u] = parent[u], parent[parent[u]]   
      return u
  ```


### unionSet
**unionSet**\(_u_,_v_\) merges the two specified sets, the set in which the element _u_ is located, and the set in which the element _v_ is located.

