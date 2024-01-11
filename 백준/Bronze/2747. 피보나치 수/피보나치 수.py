n = int(input())
a0, a1 = 0, 1
for i in range(n):
    a0, a1 = a1, a0+a1
print(a0)