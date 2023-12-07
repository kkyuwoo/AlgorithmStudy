import sys
n, k = map(int, sys.stdin.readline().split())
arr = []
cnt = 0
for i in range(n):
    arr.append(int(sys.stdin.readline().strip()))
arr.sort(reverse=True)
for i in range(n):
    cnt += k//arr[i]
    k = k % arr[i]
print(cnt)