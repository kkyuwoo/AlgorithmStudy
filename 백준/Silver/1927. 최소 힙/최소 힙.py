import sys
from queue import PriorityQueue
arr = PriorityQueue()

n = int(input())
for i in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if arr.qsize() == 0:
            print(0)
        else:
            print(arr.get())
    else:
        arr.put(x)
