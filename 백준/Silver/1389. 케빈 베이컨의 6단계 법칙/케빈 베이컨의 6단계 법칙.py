import sys

n, m = map(int, input().split())
distance = [[sys.maxsize for j in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    distance[i][i] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    distance[a][b] = 1 #a,b친구 관계는 b,a친구 관계와 동일
    distance[b][a] = 1

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if distance[i][j] > distance[i][k] + distance[k][j]:
                distance[i][j] = distance[i][k] + distance[k][j]

kevin_bacon = sys.maxsize #케빈 베이컨 수. 가장 작은 수를 구해야 하기 때문에 큰 수로 초기화
person = -1 #케빈 베이컨 수가 가장 작은 사람

for i in range(1, n+1):
    total = 0
    for j in range(1, n+1):
        total += distance[i][j] #i번째 사람의 케빈 베이컨 수
    if kevin_bacon > total:
        kevin_bacon = total
        person = i

print(person)