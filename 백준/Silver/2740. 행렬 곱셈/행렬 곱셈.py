import sys
n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, sys.stdin.readline().split())))

m, k = map(int, input().split())
B = []
for i in range(m):
    B.append(list(map(int, sys.stdin.readline().split())))

result = [[0]*k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result[i][j] += A[i][l] * B[l][j]

for i in range(n):
   for j in result[i]:
       print(j, end=' ')
   print()