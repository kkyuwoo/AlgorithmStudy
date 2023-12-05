import sys

sys.setrecursionlimit(10 ** 6)
n, m = map(int, sys.stdin.readline().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
arrive = False


def DFS(v, depth):
    global arrive
    if depth == 5:
        arrive = True
        return
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i, depth + 1)
    visited[v] = False


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
