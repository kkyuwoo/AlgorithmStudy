def solution(my_string):
    answer = []
    temp = ''
    for i in range(len(my_string)-1, -1, -1):
        temp = my_string[i] + temp
        answer.append(temp)
    answer.sort()
    return answer