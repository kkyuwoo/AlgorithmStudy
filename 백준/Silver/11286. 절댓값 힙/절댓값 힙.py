import sys
from queue import PriorityQueue
arr = PriorityQueue()
answer = []

n = int(sys.stdin.readline())

for i in range(n):
    x = int(sys.stdin.readline())
    if x != 0:
        arr.put((abs(x), x))
    else:
        if arr.empty():
            answer.append(0)
        else:
            temp = arr.get()
            answer.append(int(temp[1]))

for i in answer:
    print(i)