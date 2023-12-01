import sys
from collections import deque

deque = deque()
answer = []

n = int(sys.stdin.readline())
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    if len(arr) == 2:
        if arr[0] == 1:
            deque.appendleft(arr[1])
        else:
            deque.append(arr[1])
    else:
        if arr[0] == 3:
            if len(deque) != 0:
                answer.append(deque.popleft())
            else:
                answer.append(-1)
        if arr[0] == 4:
            if len(deque) != 0:
                answer.append(deque.pop())
            else:
                answer.append(-1)
        if arr[0] == 5:
            answer.append(len(deque))
        if arr[0] == 6:
            if len(deque) == 0:
                answer.append(1)
            else:
                answer.append(0)
        if arr[0] == 7:
            if len(deque) != 0:
                answer.append(deque[0])
            else:
                answer.append(-1)
        if arr[0] == 8:
            if len(deque) != 0:
                answer.append(deque[-1])
            else:
                answer.append(-1)

for i in answer:
    print(i)