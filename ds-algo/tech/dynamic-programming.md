# Dynamic programming

## Briefing
There are several very good references for Dynamic Programming (DP) as follows:

* [interviewbit](https://www.interviewbit.com/courses/programming/topics/dynamic-programming/)
* [topcoder](https://www.topcoder.com/community/competitive-programming/tutorials/dynamic-programming-from-novice-to-advanced/)
* [skerritt](https://skerritt.blog/dynamic-programming/)
* [itnext](https://itnext.io/introduction-to-multi-dimensional-dynamic-programming-666b095b2e7b)
* [blogarithms](https://blogarithms.github.io/articles/2019-03/cracking-dp-part-one)
* [brilliant](https://brilliant.org/wiki/problem-solving-dynamic-programming/)
* [hackerearth](https://www.hackerearth.com/practice/algorithms/dynamic-programming/introduction-to-dynamic-programming-1/tutorial/)
* [geeksforgeeks](https://www.geeksforgeeks.org/dynamic-programming/)

Dynamic programming is a technique of algorithmic design in which a problem is divided into sub-problems and results of sub-problems are combined into the result of the original problem. Results of a dynamic programming solution are often stored in a table, 1- or 2-dimensional array to avoid recalculation. There are two main approaches followning the dynamic programming technique, the top-down approach and the bottom-up one. 

- the top-down approach (memoization): using recursive technique to find solutions of sub-problems and store them into a table, when the sub-problem is encountered, its solution is taken out without recalculation.
- the bottom-up approach (tabulation): using the loop-statement to solve first sub-problems then the main problem.

Nevertheless, the core of the dynamic programming technique is, first, finding the induction formulae of the problem.

![Illustration of general dynamic programming technique](../../.gitbook/assets/dp_general.png)

The bottom-up and top-down approaches can be illustrated through the Fibonacci problems as follows:

{% tabs %}

{% tab title="Induction formulae" %}
The $$n$$-th Fibonacci number is defined as: 

$$ f[0] = 0; \quad f[1] = 1; \quad f[n] = f[n-1] + f[n-2]$$

{% endtab %}

{% tab title="Top-down approach" %}
```python
n = 100
result = [0] * (n+1)

result[0] = 0
result[1] = 1
def fibonacci_rec(n):
    if n <= 1: return n
    if result[n] != 0: return result[n]
    else:
        result[n] = fibonacci_rec(n-1) + fibonacci_rec(n-2)
        return result[n]
        
print(fibonacci_rec(n))        
```
{% endtab %}

{% tab title="Top-down approach" %}
```python
n = 100
result = [0] * (n+1) 
def fibonacci_ite1(n):
    result[0] = 0
    result[1] = 1
    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[n]
    
def fibonacci_ite2(n):
    a0, a1 = 0, 1
    for i in range(2, n + 1):
        a0, a1 = a1, a0 + a1
    return a1
    
print(fibonacci_ite1(n))
print(fibonacci_ite2(n))
```
{% endtab %}
{% endtab %}
  
It will take time to have a good feeling about DP. The next sections will provide illustrations for several DP problems to help the reader be familiar with the technique. A simple trick is using paper-and-pen to solve a sub-problem with a gradually-increasing size to come up with the inductive formulae. Once you have the formulae, coding is not that difficult anymore. 

## Illustration 01: Staircase and Coin-change
In this type of problems, the DP solution can be stored in a 1-dimensional array.

### Staircase problem
Problem statement: there is a staircase with $$N$$ steps ($$N$$ is a positive integer). You can jump over 1 or 2 steps at once. How many paths to go over the staircase if you start from the ground ?

Induction formulae: $$ path[0] = 1; \quad path[1] = 1; \quad path[n] = path[n-1] + path[n-2]$$ with $$n$$ is the number of steps of the staircase at the time of consideration and $$path$$ is the number of paths to go from the ground to the $$n$$-th step.

## Coin-change problem
A rather similar problem to the staircase problem is the coin-change problem. Problem statement: given an amount of money and $$N$$ type of coins (with the unlimited amount of each coins). Count and print out the number of coin changes.



## Problems for practice

* [leetcode](https://leetcode.com/tag/dynamic-programming/)
* [hackerrank](https://www.hackerrank.com/domains/algorithms?filters%5Bsubdomains%5D%5B%5D=dynamic-programming)
* [spoj](https://apps.topcoder.com/forums/?module=Thread&start=0&threadID=674592)
* [codeforces](https://codeforces.com/blog/entry/325)
* [geeksforgeeks](https://practice.geeksforgeeks.org/explore/?category%5B%5D=Dynamic%20Programming&page=1&sortBy=accuracy)
* [spoj](https://www.spoj.com/problems/tag/dynamic-programming)
* [usejournal](https://blog.usejournal.com/top-50-dynamic-programming-practice-problems-4208fed71aa3)
* 
