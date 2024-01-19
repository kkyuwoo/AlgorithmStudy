def solution(answers):
    answer = []
    num_1 = [1, 2, 3, 4, 5] * 2000
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5] * 2000
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 2000
    
    result_1 = 0
    result_2 = 0
    result_3 = 0
    result = 0
    for i in range(len(answers)):
        if num_1[i] == answers[i]:
            result_1 += 1
        if num_2[i] == answers[i]:
            result_2 += 1
        if num_3[i] == answers[i]:
            result_3 += 1
    result = max(result_1, result_2, result_3)
    if result == result_1:
        answer.append(1)
    if result == result_2:
        answer.append(2)
    if result == result_3:
        answer.append(3)
    answer.sort()
    return answer