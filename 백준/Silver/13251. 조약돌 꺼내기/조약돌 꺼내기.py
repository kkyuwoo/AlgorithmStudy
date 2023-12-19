color = [0] * 51
m = int(input())
D = list(map(int, input().split()))
T = sum(D)

K = int(input())
answer = 0

for i in range(m):
    if D[i] >= K:
        color[i] = 1
        for j in range(K):
            color[i] = color[i] * (D[i]-j) / (T-j)
        answer += color[i]

print(answer)