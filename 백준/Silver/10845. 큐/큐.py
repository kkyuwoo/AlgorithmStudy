import sys
from collections import deque

n = int(input())
array = deque()
for i in range(n):
    question = list(sys.stdin.readline().split())
    if question[0] == 'push':
        array.append(int(question[1]))
    elif question[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.popleft())
    elif question[0] == 'size':
        print(len(array))
    elif question[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif question[0] == 'front':
        if len(array) == 0:
            print(-1)
        else:
            print(array[0])
    elif question[0] == 'back':
        if len(array) == 0:
            print(-1)
        else:
            print(array[-1])