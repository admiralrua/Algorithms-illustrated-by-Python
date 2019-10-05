import random

def quicksort(a):
    if len(a) <= 1:
        return a
    
    pivot  = a[len(a) // 2]
    
    left   = [x for x in a if x <  pivot]
    middle = [x for x in a if x == pivot]
    right  = [x for x in a if x >  pivot]
    
    return quicksort(left) + middle + quicksort(right)

n = 1000
print(quicksort([random.randint(0, n//1.5) for _ in range(n)]))