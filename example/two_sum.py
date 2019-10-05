import random

n, t = 1000, 800
a = [random.randint(0,n) for _ in range(n)]
a.sort()
k = []

le, ri = 0, n-1
while (le < ri):
    x = a[le] + a[ri]
    
    if (x == t):
        k.append([le, ri])
        if (a[le] == a[le+1]):
            le += 1
        elif (a[ri] == a[ri-1]):
            ri -= 1
        else:
            le += 1
            ri -= 1
    elif (x < t):
        le += 1
    else:
        ri -= 1

for v in k:
    print(v[0], v[1])
