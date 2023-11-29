import sys
n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
total = 0
sum_arr = []
answer = 0
C = [0] * m

for i in range(n):
    total += arr[i]
    sum_arr.append(total)

for i in range(n):
    r = sum_arr[i] % m
    if r == 0:
        answer += 1
    C[r] += 1

for i in C:
    answer += i*(i-1)//2
    
print(answer)