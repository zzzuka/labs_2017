def hamilton(v):
    way.append(v)
    if len(way) == n:
        if way[-1] in A[way[0]]:
            return way
        else:
            way.pop()
            return False
    visited[v] = True
    for next in range(n):
        if next in A[v] and not visited[next]:
            if hamilton(next):
                return way
    visited[v] = False
    way.pop()
    return False

n, m = map(int, input().split())
visited = [False] * n
way = []
A = [[] for i in range(n)]
W = [[[0] for i in range(n)] for j in range(n)]
res = {}

for i in range(m):
    v1, v2, w = map(int, input().split())
    A[v1].append(v2)
    A[v2].append(v1)
    W[v1][v2] = w
    W[v2][v1] = w

for i in range(n):
    x = hamilton(i)
    sum = 0
    for j in range(n-1):
        sum += W[x[j]][x[j + 1]]
    sum += W[way[-1]][way[0]]
    res.update({sum: x})
    visited = [False] * n
    way = []

k = min(res.keys())
print(k)
print(*res[k])