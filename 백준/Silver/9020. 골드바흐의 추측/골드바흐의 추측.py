import sys

t = int(sys.stdin.readline())


def is_prime(n):
    if n == 1:
        return False
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    return True


for i in range(t):
    n = int(sys.stdin.readline())

    a, b = n // 2, n // 2

    while a > 0:
        if is_prime(a) and is_prime(b):
            print(a, b)
            break

        else:
            a -= 1
            b += 1
            