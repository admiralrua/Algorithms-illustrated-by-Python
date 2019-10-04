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
- $$T(n) = n + \frac{n}{2} + \frac{n}{4} + ... + 2 + 1 = 2*n - 1 \rightarrow O(n) = n$$
  ```python
  cnt, i, j = 0, n, 0
  while (i < n):
      for j in range(i):
          cnt += 1
          i /= 2
  ```
- $$O(n) = n*log(n)$$
  ```python
  cnt, x = 0, n
  while (x > 1):
      for j in range(n,0,-1):
          cnt += 1
          x /= 2
  ```
- $$T(n) = \frac{n*(n-1)}{2} \rightarrow O(n) = n^2$$
  ```python
  cnt = 0
  for i in range(n):
      for j in range(i):
          cnt += i*j + i + j
  ```
- $$O(n) = 2^n$$
  ```python
  def fibo(n):
      if (n == 0) or (n == 1):
          return 1
      else:
          return fibo(n-1) + fibo(n-2) 
  ```
  
Please practice with the following codes:
- Calculate $$T(n)$$ and $$O(n)$$
  ```python
  cnt = 0
  for i in range(n):
      cnt += 1
  for i in range(m):
      cnt -= 1
  ```
  ```python
  cnt = 0
  for i in range(n):
      for j in range(n):
          cnt += 1
  for i in range(n*2):
      cnt -= 1
  ```
  ```python
  x = 0
  for i in range(n//2, n+1):
      j = 1
      while (j <= n):
          x += n//2
          j *= 2
  ```
- Which loop finishes first ?
  ```python
  for i in range(n):
  ```
  ```python
  for i in range(0,n,2):
  ```
  ```python
  i = 1
  while (i <= n):
      i *= 2
  ```
  ```python    
  i = n
  while (i > -1):
      i //= 2 
  ```    

Here is a table prepared by Dr. Jeyakesavan Veerasamy to illustrate the real-life time elapsed based on the time complexity of a code and the magnitude of data involved:

--------------------------------------------------------------------------------------------------------------------------
|  $$n$$     |  $$O(1)$$      |  $$O(\log_2 n)$$  |  $$O(n)$$      |  $$O(n \log_2 n)$$  |  $$O(n^2)$$    |  $$O(2^n)$$  |
--------------------------------------------------------------------------------------------------------------------------
|  100       |  1.0 $$\mu$$s  |  1.0 $$\mu$$s     |  1.0 $$\mu$$s  |  1.0 $$\mu$$s       |  1.0 $$\mu$$s  |  1 $$\mu$$s  |
|  110       |  1.0 $$\mu$$s  |                   |                |                     |  1.2 $$\mu$$s  |  1 ms        |
|  120       |  1.0 $$\mu$$s  |                   |                |                     |  1.4 $$\mu$$s  |  1 s         |
|  130       |  1.0 $$\mu$$s  |                   |                |                     |  1.7 $$\mu$$s  |  18 m        |
|  140       |  1.0 $$\mu$$s  |                   |                |                     |  2.0 $$\mu$$s  |  13 d        |
|  150       |  1.0 $$\mu$$s  |                   |                |                     |  2.3 $$\mu$$s  |  37 y        |
--------------------------------------------------------------------------------------------------------------------------
|  $$10^3$$  |  1.0 $$\mu$$s  |  1.5 $$\mu$$s     |  10 $$\mu$$s   |  15 $$\mu$$s        |  100 $$\mu$$s  |              |
|  $$10^4$$  |  1.0 $$\mu$$s  |  2.0 $$\mu$$s     |  100 $$\mu$$s  |  200 $$\mu$$s       |  10 ms         |              |
|  $$10^5$$  |  1.0 $$\mu$$s  |  2.5 $$\mu$$s     |  1 ms          |  2.5 ms             |  1 s           |              |
|  $$10^6$$  |  1.0 $$\mu$$s  |  3.0 $$\mu$$s     |  10 ms         |  30 ms              |  1.7 m         |              |
|  $$10^7$$  |  1.0 $$\mu$$s  |  3.5 $$\mu$$s     |  100 ms        |  350 ms             |  2.8 h         |              |
|  $$10^8$$  |  1.0 $$\mu$$s  |  4.0 $$\mu$$s     |  1 s           |  4 s                |  11.7 d        |              |
--------------------------------------------------------------------------------------------------------------------------
