def floyd(W):
    A = [[[float('+inf') for j in range(n)] for i in range(n)] for k in range(n)]
    for i in range(n):
        for j in range(n):
            A[0][i][j] = W[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                A[k][i][j] = min(A[k - 1][i][j], A[k - 1][i][k - 1] + A[k - 1][k - 1][j])
    return A
n, m = map(int, input().split())
A = [[] for i in range(n)]
W = [[] for i in range(n)]
for i in range(m):
    v1, v2, w = map(int, input().split())
    A[v1].append([v2, w])
    A[v2].append([v1, w])
for i in range(n):
    for j in range(n):
        W[i][j] = A[i][j][1]

B = floyd(W)
S = [0] * n
for i in range(n):
    S[i] = sum(B[0][i])
print(S.index(min(S)))