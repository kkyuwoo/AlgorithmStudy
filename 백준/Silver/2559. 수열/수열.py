import sys
n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
sum_list = [0] * (n+1)

for i in range(1, n+1):
    sum_list[i] = sum_list[i-1] + array[i-1]

answer = -sys.maxsize

for i in range(n-k+1):
    total = sum_list[i+k] - sum_list[i]
    if answer < total:
        answer = total

print(answer)