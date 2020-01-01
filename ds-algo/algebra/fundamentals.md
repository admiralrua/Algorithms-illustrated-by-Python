[Reserved ^\_^](https://cp-algorithms.com/)

## Binary exponentiation
### Briefing
Binary exponentiation (also known as exponentiation by squaring) is a technique which allows to calculate $$a^n$$ using only $$O(\log{n})$$ multiplications (instead of $$O(n)$$ multiplications required by the naive approach). In fact, this technique can be applied to any operations that have the property of associativity:

$$(X \times Y) \times Z = X \times (Y \times Z)$$

Later, we will use this technique in modular multiplication (in problems related to modular arithmetic) and matrices multiplication (e.g. to calculate Fibonacci number in $$O(\log{n})$$).


### Algorithm
Raising $$a$$ to the power $$n$$ is expressed as multiplication by $$a$$ done $$n-1$$ times. However, this approach is not practical for large $$n$$ or we have to do that multiple time. Since the multiplication operator is associative, we can split the multiplication down to smaller numbers, e.g. $$a^{2*n} = a^n * a^n = (a^n)^2$$. Moreover, this is actually the idea of binary exponentiation, we can split the work using the binary representation of the exponent. 

Let's consider the following example: if we have to calculate $$7^{25}$$ and if we do that as follows $$7^25 = 7^{11001_2} = 7^{2^4} * 7^{2^3} * 7^1$$, we actually only need 4 multiplications instead of 25. Generally, since the number $$n$$ has $$\log{n} + 1$$ digits in base 2, we only need to perform $$O(\log{n})$$ multiplications if we know the power $$a^1, a^2,..., a^{\log{n}}$$.

The following recursive approach summarises the idea:

$$ a^n = \left\{\begin{matrix}
1 & n = 0 \\ 
(a^{n/2})^2 & n % 2 = 0 \\ 
(a^{n/2})^2 \times a & n % 2 = 1  
\end{matrix}\right. $$

```python
def binpowr(a, n):
    if n == 0: return 1
    ans = binpowr(a, n // 2)
    if n % 2 == 1: return ans * ans * a
    else: return ans * ans


def binpowi(a, n):
    ans = 1
    while n > 0:
        if n & 1: ans *= a
        a *= a
        n >>= 1
    return ans


a, n = 3, 1000000
print(binpowr(a, n))
print(binpowi(a, n))
```


## (Extended) Euclidean algorithm


## Linear Diophantine equations


## Modular arithmetic

```python
def bpmod(a, n, m):
    a %= m
    ans = 1
    while n > 0:
        if n & 1: ans = ans * a % m
        a = a * a % m
        n >>= 1
    return ans


a, n, m = 7, 1000000, 2019
print(bpmod(a, n, m))
```

## Problems for practice
- [uva_Modex](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
- [uva_Big Mod](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
- [uva_Leading and trailing](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
- [spoj_The last digit](https://www.spoj.com/problems/LASTDIG/)
- [spoj_Magic of the locker](https://www.spoj.com/problems/LOCKER/)
- [spoj_Just add it](https://www.spoj.com/problems/ZSUM/)
- [icpc_Jewel-eating monster](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1723)
