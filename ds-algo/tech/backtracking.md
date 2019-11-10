# Backtracking

## Briefing
[Backtracking](https://en.wikipedia.org/wiki/Backtracking) is a general algorithm for finding all solutions of a computational problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") if that candidate cannot possibly be completed to a valid solution. Backtracking can be applied only for problems which admit the concept of a _partial candidate solution_ and a relatively quick test of whether it can possibly be completed to a valid solution. 

Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for enumeration, parsing, for the knapsack problem and other combinatorial optimization problems.

There are several basic problems to illustrate the backtracking such as:

- sum-$$n$$: enumerate all methods to sum up positive integers to a certain value $$n$$; 
- knight's tour problem: find a route for the knight to travel all squares of the board once;
- $$n$$-queens puzzle: find all arrangements of $$n$$ chess queens on a chessboard size $$n \times n$$ so that no queen attacks any other
- Sudoku puzzle.

## Algorithm
With the backtracking technique, a problem is solved incrementally. 

1. We start from an empty solution vector and gradually add items. 
1. If the item added violate the problem constraint then we remove the item and try other alternatives for adding. If there is no alternatives then we come back to the previous stage and remove the item added in the previous stage. 
1. If we reach the initial stage then actually no solution exists. 
1. If adding an item doesn’t violate constraints then we recursively add items one by one. 
1. If the solution vector becomes complete then we print the solution. 

The pseudo-code of the backtracking algorithm can be presented as follows:

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

{% tabs %} {% tab title="Illustration" %}

Illustrations of the backtracking algorithm to solve the knight tour problem, the sum-$$n$$, and the $$n$$-Queen are given here. 

In the first problem, the naive backtracking solution is presented in which we backtrack only when we hit a dead end

In the last two problems, we combine the backtracking algorithm with the [branch-and-bound](https://www.geeksforgeeks.org/branch-and-bound-algorithm/) technique. After building a partial solution, we figure out that if it is possible to go any deeper or not. By doing that, obvious unacceptatble solutions are eliminated early to save time. 

In the sum-$$n$$ problem, the branch-and-bound technique can be illustrated as follows:

- use two vectors: $$\mathbf{x}$$ and $$\mathbf{s}$$ 
- vector $$\mathbf{x}$$ for a solution with a constraint $$x[i] \le x[i+1]$$ 
- vector $$\mathbf{s}$$ to store the partial sum of the solution vector, $$s[i] = \sum_{j=1}^{i} x[j]$$
- constraint $$x[i] \le x[i+1]$$ and vector $$\mathbf{s}$$ help reducing a choice of the next element of a solution vector.


In the $$n$$-Queen problem, the branch-and-bound technique can be illustrated as follows:

- no two queens can place on the same horizontal, vertical or diagonal lines;
- the first constraint can be automatcically satisfied if we place queen line-by-line;
- the second constraint can be tracked by a logical vector length $$n$$, a space of alternatives for the next item is reduced one after each placement;
- the third constraint can be controlled by two logical vectors length $$2 \times n$$ to track the left- and right-inclined diagonals, a space of alternatives for the next item is reduced atleast one after each placement.  

More information and probelms to illustrate the Branch-and-Bound technique can be found in the following links:

- [15-puzzle & knap-sack](http://www.cs.umsl.edu/~sanjiv/classes/cs5130/lectures/bb.pdf) 
- [8-puzzle & traveling saleman](https://www2.seas.gwu.edu/~bell/csci212/Branch_and_Bound.pdf)
- [job assignment](https://www.geeksforgeeks.org/job-assignment-problem-using-branch-and-bound/)
- [traveling saleman](https://www.geeksforgeeks.org/traveling-salesman-problem-using-branch-and-bound-2/) or [here](https://v1study.com/giai-thuat-va-lap-trinh-ky-thuat-nhanh-can.html)

Banch-and-Bound is a very useful technique to significantly reduce the search-space toward the correct solution. It is the best technique to solve some problems in which scanning the whole possible-solution space is a must. Examples will be given later. 

{% endtab %}

{% tab title="Knight's tour" %}

```python
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
    if (cnt == 0): print("No solution exists.")
```

{% endtab %} 

{% tab title="sum-$$n$$" %}

```python
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
```

{% endtab %}

{% tab title="Place of Queens" %}

```python
import sys
sys.setrecursionlimit(1000000)

def sol_out(position): 
    global cnt
    cnt += 1
    """
    for i in range(1,n+1): 
        for j in range(1,n+1): 
            if (j == position[i]): print(" Q".format(position[j]), end = ' ') 
            else: print(" *", end = ' ')
        print() 
    """
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
```

{% endtab %} {% endtabs %}


## Problems for practicing
- [g4g](https://www.geeksforgeeks.org/backtracking-algorithms/)
- [leetcode](https://leetcode.com/tag/backtracking/)
- [hackerearth](https://www.hackerearth.com/practice/basic-programming/recursion/recursion-and-backtracking/practice-problems/)
- [interviewbit](https://www.interviewbit.com/courses/programming/topics/backtracking/)
- [techiedelight](https://www.techiedelight.com/Category/backtracking/)
- [spoj](https://www.spoj.com/problems/tag/backtracking)

