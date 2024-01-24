def solution(s):
    answer = 0
    arr = list(s)
    for _ in range(len(s)):
        stack = []
        for i in range(len(arr)):
            if len(stack) > 0:
                if stack[-1] == '[' and arr[i] == ']':
                    stack.pop()
                elif stack[-1] == '(' and arr[i] == ')':
                    stack.pop()
                elif stack[-1] == '{' and arr[i] == '}':
                    stack.pop()
                else:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])
        if len(stack) == 0:
            answer += 1
        arr.append(arr.pop(0)) #첫 글자를 마지막 글자로
    return answer