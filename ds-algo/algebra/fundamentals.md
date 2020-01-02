This section discusses several fundamental topics of algebra. They are foundation for more sophisticated subjects in number theories, modular arithmetic... The section is mainly based on this excellent [document](https://cp-algorithms.com/).

## Binary exponentiation
### Briefing
Binary exponentiation (also known as exponentiation by squaring) is a technique which allows to calculate $$a^n$$ using only $$O(\log{n})$$ multiplications (instead of $$O(n)$$ multiplications required by the naive approach). In fact, this technique can be applied to any operations that have the property of associativity:

$$(X \cdot Y) \cdot Z = X \times (Y \cdot Z)$$

Later, we will use this technique in modular multiplication (in problems related to modular arithmetic) and matrices multiplication (e.g. to calculate Fibonacci number in $$O(\log{n})$$).


### Algorithm
Raising $$a$$ to the power $$n$$ is expressed as multiplication by $$a$$ done $$n-1$$ times. However, this approach is not practical for large $$n$$ or we have to do that multiple time. Since the multiplication operator is associative, we can split the multiplication down to smaller numbers, e.g. $$a^{2*n} = a^n * a^n = (a^n)^2$$. Moreover, this is actually the idea of binary exponentiation, we can split the work using the binary representation of the exponent. 

Let's consider the following example: if we have to calculate $$7^{25}$$ and if we do that as follows $$7^25 = 7^{11001_2} = 7^{2^4} * 7^{2^3} * 7^1$$, we actually only need 4 multiplications instead of 25. Generally, since the number $$n$$ has $$\log{n} + 1$$ digits in base 2, we only need to perform $$O(\log{n})$$ multiplications if we know the power $$a^1, a^2,..., a^{\log{n}}$$.

The following recursive approach summarises the idea:

$$ a^n = \left\{\begin{matrix}
1 & n = 0 \\ 
(a^{n/2})^2 & n \mod 2 = 0 \\ 
(a^{n/2})^2 \times a & n \mod 2 = 1  
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
### Euclidean algorithm
Given two non-negative integers $$a$$ and $$b$$, we have to find their GCD (greatest common divisor), i.e. the largest number which is a divisor of both $$a$$ and $$b$$. It's commonly denoted by $$gcd(a,b)$$. If one number is zero, the greatest common divisor is the other number; if both numbers are zero, their GCD is undefined.

The Euclidean algorithm is stated as follows:

$$ \text{gcd}(a,b) = \left\{\begin{matrix}
a & b = 0 \\ 
\text{gcd}(b, a \mod b) & \text{otherwise} 
\end{matrix}\right. $$

The Euclidean algorithm works in $$O(\log{\min{(a,b)}})$$. Conveniently, the least common multiple (denoted as LCM) can be reduced to calculating the GCD as follows:

$$\text{lcm}(a,b) = \frac{a*b}{\text{gcd}(a,b)}$$

```python
def gcdr(a, b):
    if b == 0: return a
    else: return gcdr(b, a % b)


def gcdi(a, b):
    while b != 0:
        a %= b
        a, b = b, a
    return a


def lcm(a,b):
    return a//gcdi(a,b) * b


a, b = 1983, 2907
print(gcdr(a, b), gcdi(a, b), lcm(a,b))
```

### Extended Euclidean algorithm
When the Euclidean algorithm calculates only the greatest common divisor (GCD) of two integers $$a$$ and $$b$$, the extended version also finds a way to represent GCD in terms of $$a$$ and $$b$$, i.e. coefficients $$x$$ and $$y$$ for which:

$$ a \times x + b \times y = \text{gcd}(a,b) $$

Mathematically, the extension from the original algorithm can be expressed as follows:

- assume we found $$(x_1, y_1)$$ for $$(b \mod a, a)$$ satisfied: $$ (b \mod a) \cdot x_1 + a \cdot y_1 = g $$
- and we want to find a pair $$(x, y)$$ for $$(a, b)$$ satisfied: $$ a \times x + b \cdot y = g $$
- by substitution $$b \mod a = b - \left \lfloor \frac{b}{a} \right \rfloor \cdot a$$ we come up with the relationship:

$$ \left\{\begin{matrix}
x = y_1 - \left \lfloor \frac{b}{a} \right \rfloor \cdot x_1 \\ 
y = x_1
\end{matrix}\right. $$

- and remember that we have the base condition $$(x,y) = (0,1)$$ for $$(a,b) = (0,b)$$

```python
def egcdr(a, b):
    if a == 0:
        x, y = 0, 1
        return b, x, y
    d, x_, y_ = egcdr(b % a, a)
    x = y_ - b//a * x_
    y = x_
    return d, x, y


def egcdi(a, b):
    x1, y1 = 0, 1
    x2, y2 = 1, 0
    x, y = 1, 0

    while b != 0:
        q = a // b
        r = a % b
        x = x2 - q*x1
        y = y2 - q*y1
        x2, y2 = x1, y1
        x1, y1 = x, y
        a, b = b, r

    return a, x2, y2


a, b = 1234567, 89012
print(egcdr(a,b), ' vs ', egcdi(a,b))
```

## Linear Diophantine equations
A Linear Diophantine equation (for two variables) is an equation of the general form:

$$a \cdot x + b \cdot y = c$$

where $$a, b, c$$ are given and $$x, y$$ are unknown. In general, this equation either has no solution $$(a = b = 0; c >< 0)$$ or infinite solutions. In practice, several classical scenarios of these equations are of interested:

- finding one (and all) solutions;
- finding a solution with minimum value of $$x+y$$;
- finding the number of solutions and solutions themselves in a given interval.


## Problems for practice
- [uva_Modex](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
- [uva_Big Mod](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
- [uva_Leading and trailing](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
- [spoj_The last digit](https://www.spoj.com/problems/LASTDIG/)
- [spoj_Magic of the locker](https://www.spoj.com/problems/LOCKER/)
- [spoj_Just add it](https://www.spoj.com/problems/ZSUM/)
- [icpc_Jewel-eating monster](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1723)
- [uva_Euclid problem](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1045)
- [uva_Gift dilemma](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=4628)
- [spoj_Crucial equation](https://www.spoj.com/problems/CEQU/)
- [cf_The equation](http://codeforces.com/problemsets/acmsguru/problem/99999/106)
- [cf_Ebony and Ivory](http://codeforces.com/contest/633/problem/A)
- [cc_Get AC in one go](https://www.codechef.com/problems/COPR16G)
- [lightoj_Solutions to an equation](http://www.lightoj.com/volume_showproblem.php?problem=1306)

