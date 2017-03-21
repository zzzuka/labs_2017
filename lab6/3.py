n, m = map(int, input().split())
edges = []
for i in range(m):
    v1, v2, weight = map(int, input().split())
    edges.append([weight, v1, v2])
    edges.append([weight, v2, v1])
edges.sort()
comp = [i for i in range(n)]
res = 0
Q = []
for weight, v1, v2 in edges:
    if comp[v1] != comp[v2]:
        res += weight
        Q.append([v1, v2])
        x, y = comp[v1], comp[v2]
        for i in range(n):
            if comp[i] == y:
                comp[i] = x
Q.sort()
print(res)
for i in Q:
    print(*i)

