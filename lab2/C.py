def dfs(v):
    visited[v] = True
    for i in R[v]:
        if not visited[i]:
            dfs(i)

n = int(input())
m = int(input())
R = [[] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    R[v1].append(v2)

visited = [False] * n
visit_list = [False] * n
for v in range(n):
    dfs(v)
    if visited.count(True) == n:
        visit_list[v] = True
    visited = [False] * n
if visit_list.count(True) == n:
    print('YES')
else:
    print('NO')