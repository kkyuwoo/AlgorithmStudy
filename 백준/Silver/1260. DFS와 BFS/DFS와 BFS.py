import sys
from collections import deque

n, m, v = map(int, sys.stdin.readline().split())
A = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)
    A[b].append(a)

for i in range(n + 1):
    A[i].sort()


def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

DFS(v)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now = queue.popleft()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (n+1)
BFS(v)