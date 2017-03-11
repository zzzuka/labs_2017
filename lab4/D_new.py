n, m = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
A = [[1 * m + 2], [1, [] * m, 1] * n, [1 * m + 2]]
for i in range(1, n + 1):
    line = input()
    for j in range(1, m + 1):
        if line[j] == 'X':
            A[i].append(1)
        else:
            A[i].append(0)

i, j = x1, y1
visited = [[x1, y1]]
while i != x2 and j != y2:
    if A[i][j] == 0 and i-1 not in visited and j not in visited:
        continue #needs fixing