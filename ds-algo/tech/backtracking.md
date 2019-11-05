# Backtracking

## Briefing
[Backtracking](https://en.wikipedia.org/wiki/Backtracking) is a general algorithm for finding all solutions of a computational problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") if that candidate cannot possibly be completed to a valid solution. Backtracking can be applied only for problems which admit the concept of a _partial candidate solution_ and a relatively quick test of whether it can possibly be completed to a valid solution. 

Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems.

A classic example of the use of backtracking is the knight's tour problem that asks to find a route for the knight to travel all squares of the board once. Another typical prolem is the $$n$$-queens puzzle that asks for all arrangements of $$n$$ chess queens on a chessboard size $$n \times n$$ so that no queen attacks any other. More recently, the Sudoku problem can also be considered as a typical backtracking problem.

## Algorithm
With the backtracking technique, a problem is solved incrementally. We start from an empty solution vector and gradually add items. If the item added violate the problem constraint then we remove the item and try other alternatives for adding. If there is no alternatives then we come back to the previous stage and remove the item added in the previous stage. If we reach the initial stage then actually no solution exists. If adding an item doesn’t violate constraints then we recursively add items one by one. If the solution vector becomes complete then we print the solution. The pseudo-code of the backtracking algorithm can be presented as follows:

```python
solution = {}

def backtracking(solution)
    if (solution == complete)
        print(solution)
        return
    
    for item in possible_item:
        solution += item
        backtracking(solution)
        solution -= item
```

{% tabs %} 
{% tab title="Intro" %}

Illustration of the backtracking algorithm to solve the knight tour problem and the $$n$$-queen problem is given here.

{% endtab %}

{% tab title="Knight's tour" %}
```python
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
```
{% endtab %} 

{% tab title="$$n$$-Queen" %}

```python
```

{% endtab %}

{% endtabs %}


## Problems for practicing
- [g4g](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [leetcode](https://leetcode.com/tag/backtracking/)
- [hackerearth](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/)
- [interviewbit](https://www.interviewbit.com/courses/programming/topics/backtracking/)
- [techiedelight](https://www.techiedelight.com/Category/backtracking/)
- [spoj](https://www.spoj.com/problems/tag/backtracking)

