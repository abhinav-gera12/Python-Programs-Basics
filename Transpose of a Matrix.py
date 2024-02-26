# Transpose of a Matrix

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

Transpose = [[0,0,0],
             [0,0,0],
             [0,0,0]]

rows_A = len(A)
column_A = len(A[0])

for rows in range(rows_A):
    for columns in range(column_A):
        Transpose[columns][rows] = A[rows][columns]

for t in Transpose:      
    print(t)

