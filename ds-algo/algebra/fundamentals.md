[Reserved ^\_^](https://cp-algorithms.com/)

## Binary exponentiation
### Briefing
Binary exponentiation (also known as exponentiation by squaring) is a technique which allows to calculate $$a^n$$ using only $$O(\log{n})$$ multiplications (instead of $$O(n)$$ multiplications required by the naive approach). In fact, this technique can be applied to any operations that have the property of associativity:

$$(X \times Y) \times Z = X \times (Y \times Z)$$

Later, we will use this technique in modular multiplication (in problems related to modular arithmetic) and matrices multiplication (e.g. to calculate Fibonacci number in $$O(\log{n})$$).


### Algorithm
Raising $$a$$ to the power $$n$$ is expressed as multiplication by $$a$$ done $$n-1$$ times. However, this approach is not practical for large $$n$$ or we have to do that multiple time. Since the multiplication operator is associative, we can split the multiplication down to smaller numbers, i.e. $$a^{2*n} = a^n * a^n = (a^n)^2$$. Moreover, this is actually the idea of binary exponentiation, we can split the work using the binary representation of the exponent. 


## (Extended) Euclidean algorithm


## Linear Diophantine equations


## Modular arithmetic


## Problems for practice
- [uva_Modex](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=3671)
- [uva_Big Mod](https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=24&page=show_problem&problem=310)
- [uva_Leading and trailing](https://onlinejudge.org/index.php?option=onlinejudge&page=show_problem&problem=1970)
- [spoj_The last digit](https://www.spoj.com/problems/LASTDIG/)
- [spoj_Magic of the locker](https://www.spoj.com/problems/LOCKER/)
- [spoj_Just add it](https://www.spoj.com/problems/ZSUM/)
- [icpc_Jewel-eating monster](https://icpcarchive.ecs.baylor.edu/index.php?option=com_onlinejudge&Itemid=8&page=show_problem&problem=1723)
