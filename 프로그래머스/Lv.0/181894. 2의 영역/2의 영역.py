def solution(arr):
    answer = []
    left = -1
    right = -1
    for i in range(len(arr)):
        if arr[i] == 2:
            left = i
            break
    for i in range(len(arr)-1, -1, -1):
        if arr[i] == 2:
            right = i
            break
    if left == -1:
        answer.append(-1)
    else:
        answer = arr[left:right+1]
    return answer