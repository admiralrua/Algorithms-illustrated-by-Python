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
