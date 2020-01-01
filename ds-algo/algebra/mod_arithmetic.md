## Basic operators

### Multiplication
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

## Modular inverse

__more__
