def bfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    cycles = [[start]]
    visited.add(start)
    queue = [start]
    while queue.pop(0) != start:
        v = queue.pop(0)
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                cycles.append(neighbour)

    return cycles

n, m = map(int, input().split())
A = [[] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    A[v1].append(v2)

k = 100000000000
for i in range(n):
    if min(len(bfs(A, i))) < k:
        k = min(bfs(A, i))
if k == 0:
    print('NO CYCLES')
else:
    print(k)
