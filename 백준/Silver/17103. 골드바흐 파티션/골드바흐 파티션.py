import sys

t = int(sys.stdin.readline())
is_prime = [True for i in range(1000001)]

for i in range(2, int(1000000**0.5)+1):
    if is_prime[i]:
        for j in range(2*i, 1000001, i):
            is_prime[j] = False

for i in range(t):
    result = 0
    n = int(sys.stdin.readline())

    a, b = n // 2, n // 2

    for j in range(2, n//2+1):
        if is_prime[j] and is_prime[n-j]:
            result += 1
    print(result)