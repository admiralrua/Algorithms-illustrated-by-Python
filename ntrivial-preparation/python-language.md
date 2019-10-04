---
description: 'Python is really convenient :)'
---

# Python programming language

## Brief introduction

In this note, **Python 3.x** will be used to illustrate data structures and algorithms discussed. If you, accidentally, read this note, I guess you already know that Python is a high-level, dynamically typed multi-paradigm programming language.

Python is so friendly in the sense that it is almost like pseudo-code allowing you to express ideas in a few lines of code. Please take a look at the implementation of the famous sorting method, Quick-Sort, down here in just 10 lines of code.

```python
def quicksort(a):
    if len(a) <= 1:
        return a

    pivot  = a[len(a) // 2]
    left   = [x for x in a if x <  pivot]
    middle = [x for x in a if x == pivot]
    right  = [x for x in a if x >  pivot]

    return quicksort(left) + middle + quicksort(right)

n = 100000
print(quicksort([random.randint(0, n//1.5) for _ in range(n)]))
```

I took this code [from here](http://cs231n.github.io/python-numpy-tutorial/), and you can find many nice interesting topics there as well.

Good references for Python can be found [here](https://www.w3schools.com/python/) or the book **Python notes for professionals**. A comprehensive introduction for Python can be found in [here](https://docs.python.org/3.7/contents.html), especially for comprehension syntax.

## Something I have been used quite often

In the following tables, I will give some useful syntax that I have been used quite a lot recently. This table will grow continuously \(hopefully\):

```python
# Format printing
a, b, c = 2, 3, 5
print('a_{0:.3f} + b_{1} = c_{2}'.format(a,b,c))     

# Input from keyboard
n    = int(input())                                  
n, m = map(float, input().split())
st   = list(map(str, input().split()))

# Enumerating looping
for i, v in enumerate(['tic', 'tac', 'toe']):        
    print('#%d: %s' % (i, v))

# Pair looping    
ques = ['name', 'role', 'school', 'sport', 'fav work']
answ = ['ctn', 'engineer', 'cva', 'fitness', 'coding']
reps = ['ok', 'what kind ?', 'ok', 'lazy', 'really ?']
for q, a, r in zip(ques, answ, reps):                
    print('What is your {0}?  It is {1}. -> REP: {2}'.format(q, a, r))

# List comprehension
numbers = [0, 1, 2, 3, 4]
even_sq = [x ** 2 for x in numbers if x % 2 == 0]
print(even_sq)  

# Quick plus
import random
a   = [random.randint(0, 100) for _ in range(100)]
b   = [random.randint(0, 100) for _ in range(100)]
apb = [sum(x) for x in zip(a, b)]
```

