def solution(arr, k):
    answer = []
    for i in arr:
        if i not in answer:
            if len(answer) < k:
                answer.append(i)
    if len(answer) < k:
        while len(answer) < k:
            answer.append(-1)
    return answer