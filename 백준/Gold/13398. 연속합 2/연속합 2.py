n = int(input())
arr = list(map(int, input().split()))

D = [[0] * n for i in range(2)]
D[0][0] = arr[0]

answer = arr[0]
for i in range(1, n):
    D[0][i] = max(D[0][i-1] + arr[i], arr[i])   # 직전까지의 연속 합 + 현재 값, 현재 값 중 최대(수 제거 X)
    D[1][i] = max(D[1][i-1] + arr[i], D[0][i-1])    # 이미 제거 후 현재 값 더하기, 현재 값 제거 중 최대(수 제거 O)
    answer = max(answer, D[0][i], D[1][i])
    
print(answer)