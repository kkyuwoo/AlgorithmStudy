from collections import deque

arr = deque()
n = int(input())
result = []

for i in range(1, n+1):
    arr.append(i)

while len(arr) > 1:
    result.append(arr.popleft())
    arr.append(arr.popleft())

result.append(arr.pop())

for i in result:
    print(i, end=' ')