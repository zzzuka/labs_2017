n, m, x, y = map(int, input().split())
A = [[] for i in range(n)]
for i in range(m):
    v1, v2, w = map(int, input().split())
    A[v1].append([v2, w])
    A[v2].append([v1, w])

d = [float('+inf') for v in A]
d[x] = 0
prev = [None] * n
used = [False] * n
min_d = 0
min_v = x
while min_d < float('+inf'):
    i = min_v
    used[i] = True
    for neighbour in A[i]:
        if d[i] + neighbour[1] < d[neighbour[0]]:
            d[neighbour[0]] = d[i] + neighbour[1]
            prev[neighbour[0]] = i
    min_d = float('+inf')
    for i in range(n):
        if not used[i] and d[i] < min_d:
            min_d = d[i]
            min_v = i
way = []
j = y
while j is not None:
    way.append(j)
    j = prev[j]
way = way[::-1]
print(*way)