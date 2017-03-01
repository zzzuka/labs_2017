def dfs(v, R, visited = set()):
    visited.add(v)
    for i in R[v]:
        if i not in visited:
            dfs(i, R, visited)
    O.append(v)

def turn(O):
    order_new = [0] * len(O)
    for i in range(len(O)):
        order_new[len(O) - i - 1] = O[i]
    return order_new

n = int(input())
m = int(input())
R = [[] for i in range(n)]
T = [[] for i in range(n)]
A = [[] for i in range(n)]
for i in range(m):
    v1, v2 = map(int, input().split())
    R[v1].append(v2)
    T[v2].append(v1)
    A[v1].append(v2)
    A[v2].append(v1)

visited = set()
s = 0
O = []
for v in range(len(R)):
    if v not in visited:
        dfs(v, R, visited)

O1 = turn(O)
visited1 = set()
for v in O1:
    if v not in visited1:
        dfs(v, T, visited1)
        s += 1

visited_list = set()
w = 0
for v in range(len(A)):
    if v not in visited_list:
        dfs(v, A, visited_list)
        w += 1

print(w, s)