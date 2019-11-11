import sys
sys.setrecursionlimit(1000000)

def sol_out(position): 
    global cnt
    cnt += 1

    for i in range(1,n+1): 
        for j in range(1,n+1): 
            if (j == position[i]): print(" Q".format(position[j]), end = ' ') 
            else: print(" *", end = ' ')
        print() 

    print("---------- ", cnt)
      
def check(i,loc):
    if (vert[i]) and (diag[loc+i-1]) and (rdiag[loc-i+n]): return True
    return False
  
def solve(position, loc): 
    if(loc == n+1): 
        sol_out(position)
        return True
      
    for i in range(1,n+1): 
        if check(i,loc):
            position.append(i)
            vert[i] = diag[loc+i-1] = rdiag[loc-i+n] = False
        
            solve(position, loc+1)
            
            vert[i] = diag[loc+i-1] = rdiag[loc-i+n] = True
            position.pop()             
        
    return False
          
if __name__ == "__main__":  
    n     = int(input())
    vert  = [True for i in range(2*n)]
    diag  = [True for i in range(2*n)]
    rdiag = [True for i in range(2*n)]
      
    position, cnt = [0], 0

    for i in range(1,n+1):
        position.append(i)
        vert[i] = diag[1+i-1] = rdiag[1-i+n] = False
        
        solve(position, 2)
        
        vert[i] = diag[1+i-1] = rdiag[1-i+n] = True
        position.pop()
        
    if (cnt == 0): print("No solution exits")