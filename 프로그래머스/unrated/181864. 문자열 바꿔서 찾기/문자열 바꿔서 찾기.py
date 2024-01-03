def solution(myString, pat):
    answer = 0
    temp = ''
    for i in myString:
        if i == 'A':
            temp += 'B'
        else:
            temp += 'A'
    if pat in temp:
        answer = 1
    return answer