import sys

n = int(sys.stdin.readline())
stack = []
answer = []
for i in range(n):
    arr = list(map(int, sys.stdin.readline().split()))
    if len(arr) == 1:
        if arr[0] == 2:
            if len(stack) > 0:
                answer.append(stack.pop())
            else:
                answer.append(-1)
        if arr[0] == 3:
            answer.append(len(stack))
        if arr[0] == 4:
            if len(stack) == 0:
                answer.append(1)
            else:
                answer.append(0)
        if arr[0] == 5:
            if len(stack) > 0:
                answer.append(stack[-1])
            else:
                answer.append(-1)
    else:
        stack.append(arr[1])

for i in answer:
    print(i)
