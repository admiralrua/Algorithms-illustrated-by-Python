import sys
sys.setrecursionlimit(1000000)

def sol_out(board): 
    global cnt
    cnt += 1

    for i in range(n): 
        for j in range(n): print("{:3d}".format(board[i][j]), end = ' ') 
        print() 

    print("----- ", cnt, " -----")
      
def check(board,new_x,new_y):
    if ((new_x in range(n)) and (new_y in range(n)) and (board[new_x][new_y] == -1)): return True
    return False
  
def solve(board,curr_x,curr_y,move_x,move_y,move): 
    # check if the current solution is accepted
    if(move == n**2): 
        sol_out(board)
        return True
      
    # try all alternatives
    for i in range(8): 
        new_x = curr_x + move_x[i]                                # generate a new item to be added to a solution space
        new_y = curr_y + move_y[i]
        
        if check(board,new_x,new_y):                              # check if a new item can be added
            board[new_x][new_y] = move            
            solve(board,new_x,new_y,move_x,move_y,move + 1)       # recursive to the next item (list all solutions)          
            '''
            if solve(board,new_x,new_y,move_x,move_y,move + 1):   # recursive to the next item (only one solution is needed)
                return True
            '''            
            # backtracking 
            board[new_x][new_y] = -1                              # remove this item to try an alternative
            
    return False
          
if __name__ == "__main__":  
    # initialization of a board  
    n     = int(input())                                          # board dimension
    board = [[-1 for i in range(n)] for i in range(n)]            # map of movement
      
    # move_x and move_y define next move of the knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]                         # all possible alternatives
    move_y = [1, 2, 2, 1, -1, -2, -2, -1] 
      
    # solution 
    board[0][0] = 0                                               # put the knight at the first square
    move, cnt   = 1, 0                                            # number of move of knight         
    solve(board,0,0,move_x,move_y,move)                           # Knight's tour
    if (cnt == 0): print("No solution exits")