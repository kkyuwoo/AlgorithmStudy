import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
plus = PriorityQueue()
minus = PriorityQueue()
one = 0
zero = 0

for i in range(n):
    data = int(sys.stdin.readline())
    if data > 1:
        plus.put(data * -1)
    elif data == 1:
        one += 1
    elif data == 0:
        zero += 1
    else:
        minus.put(data)

total = 0

while plus.qsize() > 1:
    first = plus.get() * -1
    second = plus.get() * -1
    total += first * second

if plus.qsize() > 0:
    total += plus.get() * -1

while minus.qsize() > 1:
    first = minus.get()
    second = minus.get()
    total += first * second

if minus.qsize() > 0:
    if zero == 0:
        total += minus.get()

total += one
print(total)