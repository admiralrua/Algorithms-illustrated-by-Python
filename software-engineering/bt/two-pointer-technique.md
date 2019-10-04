# Two-pointer technique

## Introduction
The two-pointer algorithm refers to searching that use two pointers in one for/while loop over the given data structures. Consequently, this part of code gives a time complexity of $$O(n)$$. There are different ways to put these two pointers:
- **Same direction** both start from the beginning and may move with different increments depending on the problem;
- **Opposite direction** one at the start and the other at the end moving close to each other and meet in the middle;
- **Mixture** mixing of the above two methods. 

In order to use the two-pointer algorithm, the data structure may need to be ordered in some way. In some cases, the time complexity is highly dependable on the data and criteria of searching. Generally speaking, two-pointer algorithm can solve a large set of K-sum, sub-array and string pattern match problems. In the next sections, numerous example will be given to illustrate the algorithm. Learning an algorithm by example codes is always a not-bad way.

There are some good references for the two-pointer algorithm:
- [Quora](https://www.quora.com/q/kfhwdajorrdsqlrs/The-Two-Pointer-Algorithm)
- [Li Yin](https://medium.com/algorithms-and-leetcode/two-pointer-algorithm-explained-with-leetcode-problems-2ed289925acf)
- [Aditya Ramesh](https://blogarithms.github.io/articles/2019-04/two-pointer-algo)
- [LeetCode](https://leetcode.com/articles/two-pointer-technique/)

and many problems from different sources to practice:
- [Problems from LeetCode](https://leetcode.com/tag/two-pointers/)
- [Problems from cf](https://codeforces.com/problemset?tags=two+pointers)
- [Problems-I from G4G](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Problems-II from G4G](https://www.geeksforgeeks.org/window-sliding-technique/)


## Same direction
### Introduction
In this section, the technique will be illustrated by several problems related to the linked list.

The first problem is to find the middle node of a given linked list. The solution is quite straight forward. We place two pointers simultaneously at the head node, each one moves at different paces, the slow pointer moves one step and the fast moves two steps instead. When the fast pointer reached the end, the slow pointer will stop at the middle.

```python
def middle_Node(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        return slow
```

The next problem relating to a cycle in a linked list. Given a linked list, check if it contains a cycle. Then detect where is the first and last nodes of the cycle. Finally, remove the cycle from the list. To solve this problem we also keep the slow and fast pointers moving by one and two steps, respectively. As the pointers move, if they are at the same location ever then a cycle is detected, else not. 

```python
def has_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
        return False
```

In the problems related to cycle detection, if we want to find the starting node of the cycle, we can move the slow pointer to the start of the linked list after the meeting point, and make both both pointers to move one node at a time, they will meet at the starting node of the cycle.

```python
def first_Node_of_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
         
    slow = head
    while fast and slow != fast:
        slow = slow.next
        fast = fast.next
    return slow
```

Furthermore, if we want to remove the cycle then we need to find the last node of the cycle. Since the starting node is when slow and fast pointers intersect, the last node of the cycle is the last fast pointer before they meet.

```python
def last_Node_of_Cycle(self, head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            break
         
    slow = head
    while fast and slow.next != fast.next:
        slow = slow.next
        fast = fast.next
      
    # fast.ext = None     # use this to remove the cycle ;)
    return fast
```

Another typical example to illustrate the two-pointer technique is the merging algorithm in the Merge Sort method which maintains $$O(n \log_2 n)$$ in the worst case. The merging algorithm merges two sorted arrays into one array which should also be sorted; therefore, we actually need two pointers running in each array to choose an element of which array to be added into the new array. Please take a look into the code here:
- Merging algorithm
  ```python
  def merge(aL, aR):
      aS, nL, nR, i, j = [], len(aL), len(aR), 0, 0
      
      while (i < nL) and (j < nR):
          if (aL[i] < aR[j]):
              aS.append(aL[i])
              i    += 1
          else:
              aS.append(aR[j])
              j    += 1
              
      for i in range(i,nL):
          aS.append(aL[i])
          
      for j in range(j,nR):
          aS.append(aR[j])
          
      return aS
  ```
- Merge Sort 
  ```python
  def mergeSort(a):
      n  = len(a)-1
      
      if (n == 0):
          return a
      
      nL = int(n/2)
      
      aL = a[0:nL+1]
      aR = a[nL+1:n+1]
      
      aL = mergeSort(aL)
      aR = mergeSort(aR)
      
      a = merge(aL, aR)
      return a 
  ```


### Problems for practice
The following problems from different sources can be used to practice the slow-faster pointers algorithm:
- [cf A0161](https://codeforces.com/problemset/problem/161/A)
- [cf A0381](https://codeforces.com/problemset/problem/381/A)
- [cf B0224](https://codeforces.com/problemset/problem/224/B)
- [cf B0602](https://codeforces.com/problemset/problem/602/B)



## Opposite direction
### Introduction
In many problem, two pointers are needed to search for a pair of elements in an array and the data can be organized in a way that we can search all the result space by placing two pointers each at the start and rear of the array and move them to each other and eventually meet and terminate the search process. This way, each item in the array is guaranteed to be visited at most one time by one of the two pointers, thus making the time complexity to be $$O(n)$$.

A typical problem to illustrate for this technique can be stated as followings: given an array of integers $$a[0..n]$$, find two numbers such that they add up to a specific target number $$t$$. It is obvious that, after sorting the array in ascending order, the technique can be applied directly as following: 
- put the $$le$$ pointer at the beginning and $$ri$$ pointer at the end;
- if $$a[le] + a[ri] == t$$: found a pair;
- if $$a[le] + a[ri] < t$$, move $$le$$ to the right; otherwise, as $$a[le] + a[ri] > t$$, move $$ri$$ to the left.
- the following code print out all possible pair of integers in the array:
  ```python
  import random
  
  n, t = 1000, 800
  a = [random.randint(0,n) for _ in range(n)]
  a.sort()
  k = []
  
  le, ri = 0, n-1
  while (le < ri):
      x = a[le] + a[ri]
      
      if (x == t):
          k.append([le, ri])
          if (a[le] == a[le+1]):
              le += 1
          elif (a[ri] == a[ri-1]):
              ri -= 1
          else:
              le += 1
              ri -= 1
      elif (x < t):
          le += 1
      else:
          ri -= 1
  
  for v in k:
      print(v[0], v[1])
  ```


### Problems for practice
The following problems can be used to practice the algorithm:
- [G4G The closet pair](https://www.geeksforgeeks.org/given-two-sorted-arrays-number-x-find-pair-whose-sum-closest-x/)
- [G4G Triplets with zero sum](https://www.geeksforgeeks.org/find-triplets-array-whose-sum-equal-zero/)
- [Leetcode Palindrome string](https://leetcode.com/problems/valid-palindrome/)


## Mixture
### Introduction
Mixing of the two techniques above is employed sometimes to search for the optimal result. This section will describe some variations of the two-pointer algorithms.

In some problems, the dimension of the output is pre-defined, only one pointer is required and the other is just imaginary. This technique is sometimes call sliding-window. A typical example for the problem which can be solved by this technique is as follows: given an array length $$n$$ of numbers, find the maximum value of the sum of $$k$$ _consecutive_ numbers. In this problem, we need only one pointer to run from the beginning position to the position $$n-k$$-th. When the pointer is at position $$i$$, the sum is updated by subtracting the $$i$$-th number and adding the $$i+k$$-th number. 


### Problems for practice
The following problems from different sources can be used to practice the sliding-window algorithm:
- [cf B0279](https://codeforces.com/problemset/problem/279/B)
- [cf B0602](https://codeforces.com/problemset/problem/602/B)
