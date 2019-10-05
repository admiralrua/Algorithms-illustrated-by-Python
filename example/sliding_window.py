# Naive sliding-window
import random

n, k = 10000, 24
a    = [random.randint(0,n) for _ in range(n)]
ksum = sum(a[0:k])
tmp  = ksum

for i in range(1,n-k+1):
	tmp -= a[i-1]
	tmp += a[i-1+k]
	ksum = max(ksum, tmp)
		
print(ksum)
	
	