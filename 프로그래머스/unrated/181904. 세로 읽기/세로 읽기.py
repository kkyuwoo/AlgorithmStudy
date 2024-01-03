def solution(my_string, m, c):
    answer = ''
    temp = []
    for i in range(0, len(my_string), m):
        answer += my_string[i+c-1]
    return answer