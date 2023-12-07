import sys

n = int(sys.stdin.readline())
arr = [[0] * 2 for _ in range(n)]

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr[i][0] = b
    arr[i][1] = a

arr.sort()
count = 0
end = -1

for i in range(n):
    if arr[i][1] >= end:
        end = arr[i][0]
        count += 1

print(count)