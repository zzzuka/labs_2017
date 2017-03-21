def hamilton(v):
    way.append(v)
    if len(way) == n:
        if way [-1] in A[way[0]]:
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

for i in range(m):
    v1, v2 = map(int, input().split())
    A[v1].append(v2)
    A[v2].append(v1)

print(*hamilton(0))