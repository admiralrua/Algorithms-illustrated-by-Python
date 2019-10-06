# Recursion technique

## Introduction

Recursion is the process of defining something in terms of itself. Every recursive function have a recursive condition to call itself working on a smaller database/cases and a base condition that stops the recursion otherwise the function calls itself infinitely.

Recursion is a typical divide-and-conquer algorithm which will be discussed in more detailed later. Basically, it has three steps:

* **Divide** the problem is divided into smaller sub-problems;
* **Conquer** each sub-problem is solved separately;
* **Combine** solutions of sub-problems are combined to form the solution of the initial problem. 

Python seems to have a quite small number for recursion depth, so please remember to include this line in your code.

```python
import sys
sys.setrecursionlimit(1000000)
```

## Examples

The traditional examples for recursion are to calculate:

* the factorial $$n!$$

  ```python
  def fact(n):
      if (n == 0):
          return 1
      else:
          return n * fact(n-1)
  ```

* the _n_-th Fibonacci number

  ```python
  def fibo(n):
      if (n == 0) or (n == 1):
          return 1
      else:
          return fibo(n-1) + fibo(n-2)
  ```

Obvious disadvantages of recursion are: \(1\) recursive calls are inefficient as they take up a lot of memory and time; \(2\) recursive functions are hard to debug. However, for a small problem, recursive functions make the code look concise. Sometimes, one can easily find an iterative solution for the problem although the recursive solution looks more like the mathematical definition.

* the factorial $$n!$$ - iterative solution

  ```python
  def fact_iter(n):
      ans = 1
      for i in range(2,n+1):
          ans *= i    
      return ans
  ```

* the _n_-th Fibonacci number - iterative solution

  ```python
  def fibo_iter(n):
      a, b = 0, 1
      for i in range(n):
          a, b = b, a+b
      return a
  ```

The iterative solution executes much faster, especially for the Fibonacci problem. The reason is that the function is called many time for the same identical sub-problem, i.e. to calculate fibo\(5\), fibo\(1\) is called 5 times. The implementation above doesnt remember previously calculated values. This problem in the recursive approach can be tackled by the memorisation technique in which a dictionary is employed to save the solutions of sub-problems.

* the _n_-th Fibonacci number - memorisation technique

  ```python
  memo = {0:0, 1:1}
  def fibo_memo(n):
      if not n in memo:
          memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
      return memo[n]
  ```

If we check the time elapsed, it turns out that the memorisation technique is even faster than the iterative solution.

## Problems for practice

There are a couple of problems for practicing, it would be nice to come up with both naive, iterative and memorisation solutions for those. I should admit that I only work the naive solution out for several problems down there.

* Find the maximum odd divisor of a positive number. 
* Count the number of digit of a number.
* Find the first or largest digit of a number.
* Find the maximum divisor of two numbers with the value up to $$10^5$$.
* Find the largest prime number in a list of up to $$10^5$$ elements.
* Calculate the sum of even numbers in a list of up to $$10^5$$ elements.
* Solve the Hanoi's tower problem and estimate the time complexity to understand why it is mentioned quite often as a **typical** recursive problem. A nice iterative solution exists [here](https://en.wikipedia.org/wiki/Tower_of_Hanoi#Iterative_solution). 
* The list in [G4G](https://www.geeksforgeeks.org/recursion-practice-problems-solutions/) gives you a set of problems for practice with recursion on different types of data structures.

In general, the recursive method is really powerful one, especially if the memorization technique can be combined.

