import sys
sys.setrecursionlimit(number_you_need)

# Code to calculate the factorial
# n! = n * (n-1)!
def fact(n):
    if (n == 0):
        return 1
    else:
        return n * fact(n-1)
		
def fact_iter(n):
    ans = 1
    for i in range(2,n+1):
        ans *= i	
    return ans


# Code to calculate the Fibonacci number
# 0 1 1 2 3 5 8 13 21 ...	
def fibo(n):
    if (n == 0) or (n == 1):
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

def fibo_iter(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
	
memo = {0:0, 1:1}
def fibo_memo(n):
    if not n in memo:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]
