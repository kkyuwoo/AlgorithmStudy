import sys
from collections import deque

n = int(input())
array = [[] for _ in range(n+1)]
indegree = [0] * (n+1)
buildHour = [0] * (n+1)

for i in range(1, n+1):
    input_data = list(map(int, sys.stdin.readline().split()))
    buildHour[i] = input_data[0]
    index = 1
    while True:
        preTemp = input_data[index]
        index += 1
        if preTemp == -1:
            break
        array[preTemp].append(i)
        indegree[i] += 1

queue = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = [0] * (n+1)

while queue:
    now = queue.popleft()
    for i in array[now]:
        indegree[i] -= 1
        result[i] = max(result[i], result[now] + buildHour[now])
        if indegree[i] == 0:
            queue.append(i)

for i in range(1, n+1):
    print(result[i] + buildHour[i])