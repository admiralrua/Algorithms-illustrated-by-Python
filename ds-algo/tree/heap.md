# Heap

## Briefing

A [heap](https://en.wikipedia.org/wiki/Heap_(data_structure) is a specialized tree-based data structure which is essentially an almost complete tree that satisfies the **heap** property: in _a max heap_, for any given node $$C$$, if $$P$$ is a parent node of $$C$$, then the key \(the value\) of $$P$$ is greater than or equal to the key of $$C$$. In _a min heap_, the key of $$P$$ is less than or equal to the key of $$C$$. The node at the _top_ of the heap \(with no parents\) is called the _root_ node.

![Example of a max-heap](../../.gitbook/assets/image%20%281%29.png)

The heap is one maximally efficient implementation of an abstract data type called a priority queue. In a heap, the highest \(or lowest\) priority element is always stored at the root. However, a heap is not a sorted structure. A heap is a useful data structure when it is necessary to repeatedly remove the object with the highest \(or lowest\) priority.

Heap is widely used to solve numerous practical problems related to priority queue, sorting operation and graph algorithms. In this note, at the moment, only a **binary heap** is referred.

## Algorithm

Heaps are usually implemented in an array. After an element is inserted into or deleted from a heap, the heap property may be violated and the heap must be balanced by internal operations.

Binary heaps can be represented in a very space-efficient way as follows: \(1\) the first element will contain the root; \(2\) the next two elements of the array contain its children; \(3\) the next four contain the four children of the two child nodes, etc. There are four basic formulae for this type of storage:

| Item | One-based array | Zero-based array |
| :--- | :--- | :--- |
| Current item | $$i$$ | $$i$$ |
| Left-child | $$2*i$$ | $$2*i+1$$ |
| Right-child | $$2*i+1$$ | $$2*i+2$$ |
| Parent | $$i//2$$ | $$(i-1)//2$$ |

Some basic operations related to the binary heap can be listed as follows:

* Build a heap from a list, $$O(n)$$;
* Find a minimum/maximum element in a heap, $$O(1)$$; 
* Add an element to a heap, $$O(\log n)$$;
* Delete an element in a heap - actually only the first element, $$O(\log n)$$, or the last element, $$O(1)$$.

## Implementation

You have multiple choices \(in Python\) to complete heap's operations:

* Implement by yourself - not necessarily but most likely, the slowest solution;
* Use the built-in [priority queue](https://docs.python.org/3/library/queue.html?highlight=priority%20queue) platform, rather fast but not convenient for debugging; 
* Use the built-in [heapq](https://docs.python.org/3.7/library/heapq.html) library, the fastest solution and also convenient for debugging since the heap is stored as a conventional list.

The nice thing about implementing your own heap library is that you can understand it a little bit better and you can do something like delete a random element in a heap. A naive implementation of such operations is as follows \(the removal of an arbitrary element is left as a homework\):

* Correctly place an element in a heap

  ```python
  def minmax_Heapify(i, heap, opt):
      here = i
      left = i * 2 + 1
      righ = i * 2 + 2

      if (left < len(heap)) and \
         (((opt == 'max') and (heap[left] > heap[here])) or \
          ((opt == 'min') and (heap[left] < heap[here]))):
          here = left

      if (righ < len(heap)) and \
         (((opt == 'max') and (heap[righ] > heap[here])) or \
          ((opt == 'min') and (heap[righ] < heap[here]))):
          here = righ

      if (here != i):
          heap[i], heap[here] = heap[here], heap[i]
          minmax_Heapify(here, heap, opt)
  ```

* Add an element to a heap

  ```python
  def pushHeap(value, heap, opt):
      heap.append(value)
      i = len(heap) - 1

      while (i != 0) and \
            (((opt == 'max') and (heap[(i-1)//2] < heap[i])) or \
             ((opt == 'min') and (heap[(i-1)//2] > heap[i]))):
          heap[i], heap[(i-1)//2] = heap[(i-1)//2], heap[i]
          i = (i-1)//2
  ```

* Build a heap

  ```python
  def buildHeap(n, heap, opt):
      for i in range(n//2 - 1, -1, -1):
          minmax_Heapify(i, heap, opt)
  ```

* Delete the first element of a heap

  ```python
  def popHeap(heap, opt):
      length = len(heap)

      if (length == 0):
          return

      heap[0] = heap[length-1]    
      heap.pop()

      if len(heap) > 1:
          minmax_Heapify(0, heap, opt)
  ```

* Example with a heap

  ```python
  opt  = 'min'
  tmp  = [0, 2, 4, 6, 10, 12, 1, 5, 7, 9, 11, 13]
  print(tmp)

  buildHeap(len(tmp), tmp, opt)
  print(tmp)

  pushHeap(3, tmp, opt)
  pushHeap(8, tmp, opt)
  print(tmp)

  popHeap(tmp, opt) 
  print(tmp)
  ```

* Similar example but using heapq now

  ```python
  from heapq import heapify, heappush, heappop
  tmp = [0, 2, 4, 6, 10, 12, 1, 5, 7, 9, 11, 13]
  heapify(tmp)
  print(tmp)

  heappush(tmp, 3)
  heappush(tmp, 8)
  print(tmp)

  heappop(tmp)
  print(tmp)
  ```

* Please note that **heapq** by default implements the _min-heap_. If you want to have a _max-heap_, you can either change the sign of the value or create a new class and define operator \_\_lt\_\_ for its object.

  ```python
  class maxHeap:
        def __init__(self, value):
            self.value = value

        def __lt__(self, other):
            return self.value > other.value

  maxtmp = []
  for x in tmp:
      heappush(maxtmp, maxHeap(x))
  ```

## Problems for practice

The following problems from different sources can be used to practice the binary heap data structure:

* [cc Restaurant rating](https://www.codechef.com/problems/RRATING)
* [he Monk and multiplication](https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/monk-and-multiplication/)
* [he Roy and trending topics](https://www.hackerearth.com/practice/data-structures/trees/heapspriority-queues/practice-problems/algorithm/roy-and-trending-topics-1/)
* [hr Qheap](https://www.hackerrank.com/challenges/qheap1/problem)
* [uva Add-all](https://uva.onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1895)
* [spoj Promotion](https://www.spoj.com/problems/PRO/)

