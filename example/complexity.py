n = 100

# O(log(n))
cnt, i = 0, 1
while (i < n):
    cnt += 1
    i   *= 2
    
    
# O(n)
cnt, i, j = 0, n, 0
while (i < n):
    for j in range(i):
        cnt += 1
        i /= 2
    

# O(nlogn)
cnt, x = 0, n
while (x > 1):
    for j in range(n,0,-1):
        cnt += 1
        x /= 2



# O(n^2)
cnt = 0
for i in range(n):
    for j in range(i):
        cnt += i*j + i + j


# O(2^n)
def fibo(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)  


# O(max(n,m))
cnt = 0
for i in range(n):
    cnt += 1
for i in range(m):
    cnt -= 1


# T(n) = n^2 + 2n, O(n^2)
cnt = 0
for i in range(n):
    for j in range(n):
        cnt += 1
for i in range(n*2):
    cnt -= 1
	
	
# O(nlogn)
x = 0
for i in range(n//2, n+1):
    j = 1
    while (j <= n):
        x += n//2
        j *= 2
		
# n n/2 logn 4ever
for i in range(n):
for i in range(0,n,2):
i = 1
while (i <= n):
    i *= 2
i = n
while (i > -1):
    i //= 2    
	

