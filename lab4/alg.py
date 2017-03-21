#Floyd-Warshall
inf = 10**9
A = [[[inf] * n for i in range(n)] for k in range(n+1)]
for i in range(n):
    A[0][i][:] = W[i]
for k in range(1, n + 1):
    for i in range(n):
        for j in range(n):
            A[k][i][j] = min(A[k-1][i][j], A[k-1][k][j])


#Prima
inf = 10**9
dist = [inf] * n
dist[0] = 0
used = False * n
used[0] = True
tree = []
tree_weight = 0
for i in range(n):
    min_d = inf
    for j in range(n):
        if not used[j] and dist[j] < min_d:
            min_d = dist[j]
            u = j
    tree.append((i,u))
    tree_weight += w[i][u]
    used[u] = True
    for v in range(n):
        dist[v] = min(dist[v], w[u][v])


#Kraskala
edges = []
for i in range(m):
    v1, v2, weight = map(int, input().split())
    edges.append((weight, v1, v2))
edges.sort()
comp = list(range(n))
tree = []
tree_weight = 0
for weight, v1, v2 in edges:
    if comp[v1] != comp[v2]:
        tree.append((v1, v2))
        tree_weight += weight
        for i in range(n):
            if comp[i] == comp[v2]:
                comp[i] = comp[v1]

