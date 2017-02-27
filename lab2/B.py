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
   # R[v2].append(v1)

visited = [False] * (n)
k = 0
for i in range(n):
    if not visited[i]:
        k += 1
        dfs(i)
print(k)
