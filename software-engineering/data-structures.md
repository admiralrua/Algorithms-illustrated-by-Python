# Brief on data structures

There are four basic built-in container types in Python:
 - **List** is a collection which is ordered and changeable; duplicate members.
 - **Tuple** is a collection which is ordered and unchangeable; duplicate members.
 - **Dictionary** is a collection which is unordered, changeable and indexed; no duplicate members.
 - **Set** is a collection which is unordered and unindexed; no duplicate members.

Besides, some data structured as **Linked-list**, **Stacks**, **Queue** are also very powerful and widely used in practice. 

And of course we should mention **Data abstraction** as well, its extension is Object-Oriented Programming mindset which is really convenient. You can find numerous good and comprehensive references about OOP online.

## List
**List**-type can be used as a conventional array. We can access the list items by referring to the positive/negative index number. 

```python
# List as an array
# One-dimensional
a1 = [1 2 3 4 5 6 7 8 9]
a1.append(10)             # Add an element to a list
a1.append(3.14)
a1.append('hello')

b = a1[1:4:1]             # Slicing a list to crete another list
b = a1[:4]
b = a1[1:]

print(a1[ 0])             # Print the first element
print(a1[-2])             # Print the second last element

# Multi-dimensional
matrix1 = [1 2 3 4]
matrix2 = [2 3 4 1] 
matrix3 = [3 4 1 2] 
matrix4 = [4 1 2 3]

matrix  = []
matrix.append(matrix1)    # Create multi-dimensional array
matrix.append(matrix2)
matrix.append(matrix3)
matrix.append(matrix4)  

print(len(matrix))    
print(len(matrix[0]))

# Transpose rows and columns by List-comprehension
transposed = [[row[i] for row in matrix] for i in range(4)]  

# which is equal to:
transposed = []
for i in range(4):
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
```

String is a quite handy structure in Python. And actually, string can also be considered as a list of char but immutable. 
```python
st    = input()                    # Automatically be a string
st    = "Here we; have a; string"     
st[0] = "h"                        # Error, immutable

for i, ch in enumerate(st):        # Print in a long way
    print(chr(x), ord(ch), end = " ")
	
# ASCII table:
# 0 -> 9: 48 -> 57
# A -> Z: 65 -> 90
# a -> z: 97 -> 122

st_01 = "hErE; wE hAvE; A strIng"  # Compare string
print(st >= st_01)
print(st.lower() == st_01.lower)

st_02 = st + " " + st_01

print(st.find("string"))           # Check substring

st_00 = st_02.split(";")
```
