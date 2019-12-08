# Syllabus for Competitive programming
The content of this section is taken from [here](https://people.ksp.sk/~misof/ioi-syllabus/).


## Mathematics
### Arithmetics and Geometry
- [x] Integers, operations (incl. exponentiation), comparison
- [x] Basic properties of integers (sign, parity, divisibility)
- [ ] Basic modular arithmetic: addition, subtraction, multiplication, division and inverse
- [ ] Prime numbers
- [x] Fractions, percentages
- [ ] Line, line segment, angle, triangle, rectangle, square, circle
- [ ] Point, vector, coordinates in the plane
- [ ] Polygon (vertex, side/edge, simple, convex, inside, area)
- [x] Euclidean distances
- [ ] Pythagorean theorem
- [ ] _Additional topics from number theory_


### Discrete Structures (DS)
#### Functions, relations, and sets

- [ ] Functions (surjections, injections, inverses, composition)
- [ ] Relations (reflexivity, symmetry, transitivity, equivalence relations, total/linear order relations, lexicographic order)
- [ ] Sets (inclusion/exclusion, complements, Cartesian products, power sets)


#### Basic logic

- [ ] First-order logic
- [ ] Logical connectives (incl. their basic properties)
- [ ] Truth tables
- [ ] Universal and existential quantification (Note: statements should avoid definitions with nested quantifiers whenever possible.)
- [ ] _Modus ponens and modus tollens_


#### Proof techniques

- [ ] Notions of implication, converse, inverse, contrapositive, negation, and contradiction


#### Basics of counting

- [x] Counting arguments (sum and product rule, arithmetic and geometric progressions, Fibonacci numbers)
- [x] Permutations and combinations (basic definitions)
- [ ] Factorial function, binomial coefficients
- [ ] _Inclusion-exclusion principle_
- [ ] _Pigeonhole principle_
- [ ] _Pascal's identity, Binomial theorem_


#### Graphs and trees

- [x] Trees and their basic properties, rooted trees
- [ ] Undirected graphs (degree, path, cycle, connectedness, Euler/Hamilton path/cycle, handshaking lemma)
- [ ] Directed graphs (in-degree, out-degree, directed path/cycle, Euler/Hamilton path/cycle)
- [x] Spanning trees
- [x] Traversal strategies
- [ ] Decorated graphs with edge/node labels, weights, colors
- [ ] Multigraphs, graphs with self-loops
- [ ] Bipartite graphs
- [ ] _Planar graphs_


#### Discrete probability

- [ ] _Applications where everything is finite_ (hence arguments about probability can be easily turned into combinatorial arguments)

### Other areas in mathematics

- [ ] _Geometry in three or more dimensions_
- [ ] _Linear algebra, including (but not limited to) matrix multiplication, exponentiation, inversion, and Gaussian elimination, Fast Fourier transform_
- [ ] _Calculus_
- [ ] _Theory of combinatorial games, e.g., NIM game, Sprague-Grundy theory_
- [ ] _Statistics_


## Computing science

### Programming fundamentals

#### Fundamental programming constructs(for abstract machines)

- [x] Basic syntax and semantics of a higher-level language
- [x] Variables, types, expressions, and assignment
- [x] Simple I/O
- [x] Conditional and iterative control structures
- [x] Functions and parameter passing
- [x] Structured decomposition

#### Algorithms and problem-solving

- [ ] Problem-solving strategies (understand-plan-do-check, separation of concerns, generalization, specialization, case distinction, working backwards, etc.)
- [x] The role of algorithms in the problem-solving process
- [x] Implementation strategies for algorithms
- [x] Debugging strategies
- [ ] The concept and properties of algorithms (correctness, efficiency)

#### Fundamental data structures

- [x] Primitive types (boolean, signed/unsigned integer, character)
- [x] Arrays (incl. multicolumn dimensional arrays)
- [x] Strings and string processing
- [x] Static and stack allocation (elementary automatic memorymanagement)
- [ ] Linked structures
- [ ] Implementation strategies for graphs and trees
- [ ] Strategies for choosing the right data structure
- [ ] Elementary use of real numbers in numerically stable tasks
- [x] The floating-point representation of real numbers, the existence of precision issues
- [ ] Pointers and references
- [x] _Data representation in memory_
- [x] _Heap allocation_
- [ ] _Runtime storage management_
- [ ] _Using fractions to perform exact calculations_
- [ ] _Non-trivial calculations on floating point numbers, manipulating precision errors_

#### Recursion

- [x] The concept of recursion
- [x] Recursive mathematical functions
- [x] Simple recursive procedures (incl. mutual recursion)
- [ ] Divide-and-conquer strategies
- [ ] Implementation of recursion
- [ ] Recursive backtracking

#### Event-driven programming

- [ ] Some competition tasks may involve a dialog with a reactive environment. Implementing such an interaction with the provided environment is necessary.


### Algorithms and complexity
#### Basic algorithmic analysis

- [ ] Algorithm specification, precondition, postcondition, correctness, invariants
- [ ] Asymptotic analysis of upper complexity bounds (informally if possible)
- [x] Big O notation
- [x] Standard complexity classes: constant, logarithmic, linear, O(nlogn), quadratic, cubic, exponential, etc.
- [ ] Time and space tradeoffs in algorithms
- [ ] Empirical performance measurements
- [ ] _Identifying differences among best, average, and worst case behaviors_
- [ ] _Little o, Omega, and Theta notation_
- [ ] _Tuning parameters to reduce running time, memory consumption or other measures of performance_
- [ ] _Asymptotic analysis of average complexity bounds_
- [ ] _Using recurrence relations to analyze recursive algorithms_

#### Algorithmic strategies

- [ ] Simple loop design strategies
- [ ] Brute-force algorithms (exhaustive search)
- [ ] Greedy algorithms
- [ ] Divide-and-conquer
- [ ] Backtracking (recursive and non-recursive), Branch-and-bound
- [ ] Dynamic programming12
- [ ] _Heuristics_
- [ ] _Finding good features for machine learning tasks (e.g. IOI 2013 Art class problem)_
- [ ] _Discrete approximation algorithms_
- [ ] _Randomized algorithms._
- [ ] _Clustering algorithms (e.g. k-means, k-nearest neighbor)_
- [ ] _Minimizing multi-variate functions using numerical approaches._

#### Algorithms

- [ ] Simple algorithms involving integers: radix conversion, Euclid's algorithm, primality test by $$O(\sqrt{n})$$ trial division, Sieve of Eratosthenes, factorization (by trial division or a sieve), efficient exponentiation
- [ ] Simple operations on arbitrary precision integers (addition, subtraction, simple multiplication)
- [ ] Simple array manipulation (filling, shifting, rotating, reversal, resizing, minimum/maximum, preffix sums, histogram, bucket sort)
- [ ] Simple string algorithms (e.g., naive substring search)
- [ ] sequential processing/search and binary search
- [ ] Quicksort and Quickselect to find the k-th smallest element
- [ ] O(n log n) worst-case sorting algorithms (heap sort, merge sort)
- [ ] Traversals of ordered trees (pre-, in-, and post-order)
- [ ] Depth- and breadth-first traversals
- [ ] Applications of the depth-first traversal tree, such as topological ordering and Euler paths/cycles
- [ ] Finding connected components and transitive closures.
- [ ] Shortest-path algorithms (Dijkstra, Bellman-Ford, Floyd-Warshall)
- [ ] Minimum spanning tree (Jarnik-Prim and Kruskal algorithms)
- [ ] O(V E) time algorithm for computing maximum bipartitematching
- [ ] Biconnectivity in undirected graphs (bridges, articulation points)
- [ ] Connectivity in directed graphs (strongly connected components)
- [ ] Basics of combinatorial game theory, winning and losing positions, minimax algorithm for optimal game playing
- [ ] _Maximum flow. Flow/cut duality theorem.
- [ ] _Lexicographical BFS, maximum adjacency search and their properties_

#### Data structures

- [x] Stacks and queues
- [x] Representations of graphs (adjacency lists, adjacency matrix)
- [x] Binary heap data structures
- [x] Representation of disjoint sets: the Union-Find data structure
- [ ] Statically balanced binary search trees. Instances of this include binary index trees (also known as Fenwick trees) and segment trees (also known as interval trees and tournament trees)
- [ ] Balanced binary search trees
- [ ] Augmented binary search trees
- [ ] O(logn) time algorithms for answering lowest common ancestor queries in a static rooted tree
- [ ] Creating persistent data structures by path copying or using fat nodes
- [ ] Composition of data structures, e.g. 2-D statically balanced binary trees
- [x] Nesting of data structures, such as having a sequence of sets
- [x] Tries
- [ ] _String algorithms and data structures: there is evidence that the inter-reducibility between KMP, Rabin-Karp hashing, suffix arrays/tree, suffix automaton, and Aho-Corasick makes them difficult to separate_
- [ ] _Heavy-light decomposition and separator structures for static trees_
- [ ] _Data structures for dynamically changing trees and their use in graph algorithms_
- [ ] _Complex heap variants such as binomial and Fibonacci heaps_
- [ ] _Using and implementing hash tables (incl. strategies to resolve collisions)_

#### Automata and grammars

- [ ] Understanding a simple grammar in Backus-Naur form
- [ ] _Formal definition and properties of finite-state machines_
- [ ] _Context-free grammars and related rewriting systems_
- [ ] _Regular expressions_

#### Advanced algorithmic analysis

- [ ] Amortized analysis
- [ ] _Online algorithms_
- [ ] _Randomized algorithms_
- [ ] _Cryptographic algorithms_
- [ ] _Parallel algorithms_

#### Geometric algorithms

- [ ] Representing points, vectors, lines, line segments
- [ ] Checking for collinear points, parallel/orthogonal vectors and clockwise turns (for example, by using dot products and cross products)
- [ ] Intersection of two lines
- [ ] Computing the area of a polygon from the coordinates of its vertices
- [ ] Checking whether a (general/convex) polygon contains a point
- [ ] Coordinate compression
- [ ] O(n log n) time algorithms for convex hull
- [ ] Sweeping line method

## Software engineering
### Software design

- [ ] Fundamental design concepts and principles
- [ ] Design patterns
- [ ] Structured design

### Using APIs
- [ ] API (Application Programming Interface) programming

### Software tools and environments

- [x] Programming environments, incl. IDE, to write and edit program texts, compile, execute and debug program

### Software validation

- [ ] Testing fundamentals, including test plan creation and test case generation
- [ ] Black-box and white-box testing techniques
- [ ] Unit, integration, validation, and system testing
- [ ] Inspections

### Software project management

- [ ] Project scheduling (especially time management)
- [ ] Risk analysis
- [ ] Software configuration management
