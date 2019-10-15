# Trie

## Briefing
A [trie](https://en.wikipedia.org/wiki/Trie), also called digital tree or prefix tree, is a kind of search tree—an ordered tree data structure used to store a dynamic set or associative array. Another good explanation of trie can be found [here](https://algs4.cs.princeton.edu/lectures/52Tries.pdf). In the example shown below, a dictionary is stored in a trie with characters are stored in nodes; at some specific nodes storing the last character of a word there is an arbitrary integer value associated with that word. In practice, a node can store more information depending on a problem to solve. 

![Example of a trie](../../.gitbook/assets/trie.png)

Applications:

- a typical application of a trie is storing predictive text or autocomplete dictionary;
- to implement approximate matching algorithms used in spell checking;
- to replace a hash table.


## Operations and implementations
Following the example shown above, a trie has many nodes, each nodes has two components: (1) a node of data, a node can connect to other nodes; (2) an integer variable which is different from 0 if its corresponding node contains the last character of a word (a key). A naive implementation of a trie in Python can be as follows:

```python
class Node:
    def __init__(self):
        self.value = 0
        self.child = dict()
```

There are four operations related to a trie: _search_, _insertion_, _deletion_ and _printing_ in a trie. 

### Insertion
The main ideas are: (1) follow links corresponding to each character in the word (key), (2) encounter a null link (last node) then create a new node, (3) encounter the last character of the word then set value in that node. 

```python
class Node:
    def __init__(self):
        self.value = 0
        self.child = dict()
```
