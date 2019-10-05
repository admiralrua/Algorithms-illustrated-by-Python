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
