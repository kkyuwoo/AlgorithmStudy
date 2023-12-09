import sys


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    result = a * b / gcd(a, b)
    print(int(result))