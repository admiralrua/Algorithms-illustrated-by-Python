# Topological sorting

## Introduction
A [topological sorting](https://en.wikipedia.org/wiki/Topological_sorting) or topological ordering of a directed graph is a linear ordering of its vertices such that for every directed edge $$u-v$$ from vertex $$u$$ to vertex $$v$$, $$u$$ comes before $$v$$ in the ordering. The following figure illustrates a graph and several possible topological sort-configurations of that graph. 

![Example of topological sorting](../../.gitbook/assets/toposort.png)

A topological sorting is possible if and only if the graph has no directed cycles, a directed acyclic graph (DAG). Any DAG has at least one topological order, and algorithms are known for constructing a topological order of any DAG in linear time.

An obvious application of topological sorting is in scheduling a sequence of jobs or tasks based on their dependencies. The jobs are represented by vertices, and there is an edge from $$u$$ to $$v$$ if job $$u$$ must be completed before job $$v$$ can be started. Then, a topological sort gives an order in which to perform the jobs. In computer science, applications of topological ordering can be found in instruction scheduling, ordering of formula cell evaluation in spreadsheets, logic synthesis...





