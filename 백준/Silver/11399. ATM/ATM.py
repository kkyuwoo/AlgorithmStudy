import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
total = 0
result = 0
for i in range(n):
    total += arr[i]
    result += total
print(result)