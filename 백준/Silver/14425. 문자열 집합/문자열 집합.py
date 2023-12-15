n, m = map(int, input().split())
arr = []
for i in range(n):
    arr.append(input())
cnt = 0
for i in range(m):
    if input() in arr:
        cnt += 1
print(cnt)