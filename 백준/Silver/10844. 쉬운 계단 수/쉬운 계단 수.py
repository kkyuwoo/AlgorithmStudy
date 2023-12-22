n = int(input())
D = [[0 for j in range(11)] for i in range(n+1)]

for i in range(1, 10):
    D[1][i] = 1

for i in range(2, n+1):
    D[i][0] = D[i-1][1] #높이가 0이면 n-1에서는 높이가 1이어야 계단 수가 가능
    D[i][9] = D[i-1][8] #높이가 9이면 n-1에서는 높이가 8이어야 계단 수가 가능
    for j in range(1, 9): #높이가 1~8이면 자신보다 한 단계 위 또는 한 단계 아래 높이 가능
        D[i][j] = D[i-1][j-1] + D[i-1][j+1]

print(sum(D[n])%1000000000)