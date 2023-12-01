import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0] * n
stack = []

for i in range(n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)

while stack:
    answer[stack.pop()] = -1

for i in answer:
    print(i, end=' ')
