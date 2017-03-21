def cyc (h, visited, element, used):
    if element in visited:
        res[:] = []
        for i in range(visited.index(element), len(visited)):
            res.append(visited[i])
        return
    if element in used:
        return
    current_visited = []
    current_visited = visited[:] + [element]
    used.add(element)
    for i in h[element]:
        cyc(h, current_visited, i, used)
        if len(res) > 0:
            break

n, m = map(int, input().split())
visited = []
used = set()
h = [[] for i in range(n)]

for j in range(m):
    v1, v2 = map(int, input().split())
    h[v1].append(v2)

res = []
for i in range(n):
    if not i in used:
        cyc(h, visited, i, used)

if len(res) > 0:
    print(*res)
else:
    print("YES")