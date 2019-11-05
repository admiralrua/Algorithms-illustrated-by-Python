# Backtracking

## Briefing
[Backtracking](https://en.wikipedia.org/wiki/Backtracking) is a general algorithm for finding all solutions of a computational problem that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") if that candidate cannot possibly be completed to a valid solution. Backtracking can be applied only for problems which admit the concept of a _partial candidate solution_ and a relatively quick test of whether it can possibly be completed to a valid solution. 

Backtracking is an important tool for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku, and many other puzzles. It is often the most convenient technique for parsing, for the knapsack problem and other combinatorial optimization problems.

A classic example of the use of backtracking is the knight's tour problem that asks to find a route for the knight to travel all squares of the board once. Another typical prolem is the $$n$$-queens puzzle that asks for all arrangements of $$n$$ chess queens on a chessboard size $$n \times n$$ so that no queen attacks any other. More recently, the Sudoku problem can also be considered as a typical backtracking problem.

## Algorithm
With the backtracking technique, a problem is solved incrementally. We start from an empty solution vector and gradually add items. If the item added violate the problem constraint then we remove the item and try other alternatives for adding. If there is no alternatives then we come back to the previous stage and remove the item added in the previous stage. If we reach the initial stage then actually no solution exists. If adding an item doesn’t violate constraints then we recursively add items one by one. If the solution vector becomes complete then we print the solution. The pseudo-code of the backtracking algorithm can be presented as follows:

```
solution = {}

procedure backtracking(solution)
    if complete(solution) then
        print(solution)
        return
    
    solution += item
    backtracking(solution)
    solution -= item
    
    if empty(solution) then
        print("No more alternative")
        return    
```


