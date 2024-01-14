def solution(strArr):
    answer = 0
    for i in range(1, 31):
        temp = 0
        for j in strArr:
            if len(j) == i:
                temp += 1
        if temp > answer:
            answer = temp
    return answer