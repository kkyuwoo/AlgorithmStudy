def solution(arr, idx):
    answer = -1
    for i in range(len(arr)):
        if arr[i] == 1:
            if i >= idx:
                answer = i
                break
    return answer