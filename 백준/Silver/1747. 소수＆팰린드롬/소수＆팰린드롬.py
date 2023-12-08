n = int(input())
A = [0] * 10000001

for i in range(2, 10000001):
    A[i] = i

for i in range(2, int(10000001 ** 0.5) + 1):
    if A[i] == 0:
        continue
    for j in range(i + i, 10000001, i):
        A[j] = 0

i = n
while True:
    check = 0
    if A[i] != 0:
        result = A[i]
        p = list(str(result))
        if len(p) == 1:
            print(A[i])
            break
        else:
            s = 0
            e = len(p) - 1
            while s < e:
                if p[s] != p[e]:
                    check = 1
                    break
                s += 1
                e -= 1
            if check == 0:
                print(A[i])
                break
    i += 1
