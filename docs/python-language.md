---
description: 'Python is really convenient :)'
---

# Python programming language

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

I took this code [from here](http://cs231n.github.io/python-numpy-tutorial/ "A really good brief of Python"), and you can find many nice interesting topics there as well.

