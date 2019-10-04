# Algorithm complexity
In computer science, the computational complexity describes the amount of time and the amount of memory it takes to run an algorithm. There are two types of complexity, time and space. As the hardware is much more powerful now, people concerns more about the time complexity, the faster the better. 

The [time complexity](https://en.wikipedia.org/wiki/Time_complexity) is commonly estimated by counting the number of elementary operations performed by the algorithm, supposing that each elementary operation takes a fixed amount of time to perform. While analysing an algorithm, we mostly consider [$O$-notation](https://en.wikipedia.org/wiki/Big_O_notation) - an upper limit of the execution time because it tells us the execution time in the worst case. To compute $O$-notation we will ignore the lower order terms, since the lower order terms are relatively insignificant for large input.

Please take a look at the following examples to understand more on how to estimate the time complexity of a code:
- $$O(n) = log(n)$$
  ```python
  cnt, i = 0, 1
  while (i < n):
      cnt += 1
      i   *= 2
  ```
