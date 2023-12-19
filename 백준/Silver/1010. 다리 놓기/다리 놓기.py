import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n, m = map(int, sys.stdin.readline().split())
    result = 1
    if n == m:
        result = 1
    else:
        for i in range(1, m+1):
            result *= i
        for i in range(1, (m-n)+1):
            result //= i
        for i in range(1, n+1):
            result //= i
    print(result)