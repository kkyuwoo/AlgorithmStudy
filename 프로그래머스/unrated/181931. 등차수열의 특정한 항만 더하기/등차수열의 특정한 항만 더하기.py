def solution(a, d, included):
    answer = 0
    arr = []
    for i in range(1, len(included)+1):
        arr.append(a + (i-1)*d)
        
    for i in range(len(included)):
        if included[i]:
            answer += arr[i]
    return answer