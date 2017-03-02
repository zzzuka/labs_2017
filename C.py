__author__ = 'student'
def bfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    time = {start:0}
    visited.add(start)
    queue = [start]
    while queue:
        v = queue.pop(0)
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                time[neighbour] = time[v] + 1
    return time


n, m, x, y = map(int, input().split())
A = [[] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    A[v1].append(v2)
    A[v2].append(v1)

B = bfs(A, x)
print(B[y])