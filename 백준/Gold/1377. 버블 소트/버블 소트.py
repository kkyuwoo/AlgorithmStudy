import sys
n = int(sys.stdin.readline())
A = []

for i in range(n):
    A.append((int(sys.stdin.readline()), i))
   
Max = 0
sorted_A = sorted(A)

for i in range(n):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max+1)