import sys
sys.setrecursionlimit(1000000)

def sol_out(k): 
    global cnt
    cnt += 1
    
    print("{:6d}".format(cnt), end = ' : ') 
    
    for i in range(1,k+1): print("{:3d}".format(x[i]), end = ' ') 
    print()
       
def solve(m): 
    last = (n - s[m-1]) // 2 + 1
    for i in range(x[m-1],last):
        x[m] = i
        s[m] = s[m-1] + i
        solve(m+1)
        
    x[m] = n - s[m-1]
    sol_out(m)
      
if __name__ == "__main__":  
    # initialization  
    n = int(input())                                          
    x = [0 for i in range(n+1)]                                 
    s = [0 for i in range(n+1)]
      
    # solution 
    cnt  = 0
    x[0] = 1
    solve(1)