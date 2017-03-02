__author__ = 'student'
def bfs(graph, start, finish, visited = None):
    if visited is None:
        visited = set()
    time = {start:0}
    visited.add(start)
    queue = [start]
    while queue.pop() != finish + 1:
        v = queue.pop(0)
        for neighbour in graph[v]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                time[neighbour] = time[v] + 1
    return time

def matrix_to_graph(A):
    graph = [[] for i in range(n)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i-1][j] == 0:
                graph[j].append(i)
                graph[i].append(j)
            elif A[i+1][j] == 0:
                graph[j].append(i)
                graph[i].append(j)
    return graph


n, m = map(int, input().split())
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
A = [[1 * m + 2], [1, [] * m, 1] * n, [1 * m + 2]]
for i in range(1, n + 1):
    line = input()
    for j in range(1, m + 1):
        if line[j] == 'X':
            A[i].append(1)
        else:
            A[i].append(0)

B = bfs(matrix_to_graph(A), x)
print(B[y])