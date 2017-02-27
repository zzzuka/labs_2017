n = int(input())
V = []
for i in range(n):
    V.append(list(map(int, input().split())))
R = []
for i in range(n):
    for j in range(n):
        if V[i][j] != 0:
            R.append([i, j, V[i][j]])
for i in range(len(R)):
    print(*R[i])
