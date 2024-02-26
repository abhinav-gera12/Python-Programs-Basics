# Addition of two matrices

A = [[1,2,3],
     [4,5,6],
     [7,8,9]]

B = [[11,12,13],
     [14,15,16],
     [17,18,19]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

rows_A = len(A)
rows_B = len(B)

column_A = len(A[0])
column_B = len(B[0])

for rows in range(rows_A):
    for columns in range(column_A):
        result[rows][columns] = A[rows][columns] + B[rows][columns]

for add in result:
    print(add)