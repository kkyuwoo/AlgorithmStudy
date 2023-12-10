import sys
from collections import deque

n, m, k, x = map(int, input().split())
A = [[] for _ in range(n+1)]
answer = []
visited = [-1] * (n+1)


def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] += 1
    while queue:
        now = queue.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                queue.append(i)


for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    A[a].append(b)

BFS(x)

for i in range(n+1):
    if visited[i] == k:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)