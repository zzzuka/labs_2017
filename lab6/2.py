def topsort(v):
    if color[v] == 2:
        return True
    if color[v] == 1:
        return False
    color[v] = 1
    for w in A[v]:
        if not topsort(w):
            return False
    color[v] = 2
    sorted.append(v)
    return True


n, m = map(int, input().split())
A = [[] for i in range(n)]
color = [[0] for i in range(n)]
sorted = []

for i in range(m):
    v1, v2 = map(int, input().split())
    A[v1].append(v2)

cyclic = False
for v in range(n):
    if not topsort(v):
        cyclic = True
if not cyclic:
    sorted.reverse()
    print(*sorted)
else:
    print('NO')