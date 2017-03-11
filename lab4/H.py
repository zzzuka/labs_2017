__author__ = 'student'
A = [[[float('+inf') for j in range(3)] for i in range(3)] for k in range(3)]
for i in range(3):
    for j in range(3):
        A[0][i][j] = 8
print(A)
