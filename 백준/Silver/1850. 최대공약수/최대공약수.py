def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


a, b = map(int, input().split())
result = int(gcd(a, b))

for i in range(result):
    print(1, end='')