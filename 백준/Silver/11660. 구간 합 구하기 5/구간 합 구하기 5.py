import sys
n, m = map(int, sys.stdin.readline().split())
arr = [[0] * (n+1)]
sum_arr = [[0] * (n+1) for _ in range(n+1)]

for _ in range(n):
    a_row = [0] + list(map(int, sys.stdin.readline().split()))
    arr.append(a_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        sum_arr[i][j] = sum_arr[i][j-1] + sum_arr[i-1][j] - sum_arr[i-1][j-1] + arr[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(sum_arr[x2][y2] - sum_arr[x1-1][y2] - sum_arr[x2][y1-1] + sum_arr[x1-1][y1-1])