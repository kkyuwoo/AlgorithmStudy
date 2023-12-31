import sys
n, m = map(int, input().split())
sol = 0
for i in range(n):
    array = list(sys.stdin.readline().strip())
    temp = 0
    for j in array:
        if j == 'O':
            temp += 1
    if temp > m//2:
        sol += 1

print(sol)