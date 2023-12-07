import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
arr = PriorityQueue()
answer = 0

for i in range(n):
    arr.put(int(sys.stdin.readline()))

while arr.qsize() > 1:
    data1 = arr.get()
    data2 = arr.get()
    temp = data1 + data2
    answer += temp
    arr.put(temp)

print(answer)