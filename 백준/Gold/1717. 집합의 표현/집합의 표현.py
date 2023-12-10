import sys
sys.setrecursionlimit(100000)
n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n+1)


def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]


def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a


def checkSame(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(n+1):
    parent[i] = i

for i in range(m):
    question, a, b = map(int, sys.stdin.readline().split())
    if question == 0:
        union(a, b)
    else:
        if checkSame(a, b):
            print("YES")
        else:
            print("NO")