import sys
from collections import deque

n, m = map(int, input().split())
array = [[] for _ in range(n+1)]
indegree = [0] * (n + 1)

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    array[a].append(b)
    indegree[b] += 1

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

while queue:
    now = queue.popleft()
    print(now, end=' ')
    for i in array[now]:
        indegree[i] -= 1
        if indegree[i] == 0:
            queue.append(i)