import sys

n, m = map(int, input().split())
D = [[0 for j in range(1001)] for i in range(1001)]
answer = 0
for i in range(n):
    numbers = list(sys.stdin.readline().strip())
    for j in range(m):
        D[i][j] = int(numbers[j])
        if D[i][j] == 1 and j > 0 and i > 0:    # D[i][j]값이 1이면
            D[i][j] = min(D[i-1][j-1], D[i-1][j], D[i][j-1]) + D[i][j]  # 자신의 위, 왼쪽, 대각선 위의 값 중 최솟값 + 1한 값을 저장
        if answer < D[i][j]:
            answer = D[i][j]

print(answer*answer)