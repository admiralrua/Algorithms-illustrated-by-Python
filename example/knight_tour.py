import sys
sys.setrecursionlimit(1000000)

def sol_out(board): 
    for i in range(n): 
        for j in range(n): 
            print("{:3d}".format(board[i][j]), end = ' ') 
        print() 
    print("----------")
    
  
def check(board,new_x,new_y):
    if ((new_x in range(n)) and (new_y in range(n)) and (board[new_x][new_y] == -1)):
        return True
    return False

  
def solve(board,curr_x,curr_y,move_x,move_y,move): 
    if(move == n**2): 
        sol_out(board)
        return True
      
    # try all next moves
    for i in range(8): 
        new_x = curr_x + move_x[i] 
        new_y = curr_y + move_y[i]
        
        if check(board,new_x,new_y): 
            board[new_x][new_y] = move
            
            solve(board,new_x,new_y,move_x,move_y,move + 1)       # list all solutions
            
            '''
            if solve(board,new_x,new_y,move_x,move_y,move + 1):   # only one solution is needed
                return True
            '''
            
            # backtracking 
            board[new_x][new_y] = -1
            
    return False

          
if __name__ == "__main__":  
    n = int(input())
    
    # initialization of a board  
    board = [[-1 for i in range(n)] for i in range(n)] 
      
    # move_x and move_y define next move of the knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
      
    # put the knight at the first square 
    board[0][0] = 0
      
    # number of move of knight 
    cnt  = 0
    move = 1
      
    # backtracking
    solve(board,0,0,move_x,move_y,move)
