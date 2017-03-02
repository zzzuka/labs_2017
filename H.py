__author__ = 'student'
from heapq import *


def dijkstra(A, start):
    d = [float('+inf') for v in A]
    d[start] = 0
    Q = [(start, 0)]
    visited = set()
    while len(visited) != n:
        current, d_c = heappop(Q)
        if d_c != d[current]:
            continue
        for neighbour in A[current]:
            l = d_c + neighbour[1]
            if l < d[neighbour[0]]:
                d[neighbour[0]] = l
                heappush(Q, (neighbour[0], l))
        visited.add(current)
    return d

n, m, x, y = map(int, input().split())
A = [[] for i in range(n)]
for i in range(m):
    v1, v2, w = map(int, input().split())
    A[v1].append([v2, w])
    A[v2].append([v1, w])

B = dijkstra(A, x)
way = [y]
v = y
while v != x:
    if 
print(B)