def solution(myStr):
    answer = []
    temp = ''
    for i in range(len(myStr)):
        if myStr[i] == "a" or myStr[i] == 'b' or myStr[i] == 'c':
            if len(temp) != 0:
                answer.append(temp)
            temp = ''
        else:
            temp += myStr[i]
    if len(temp) != 0:        
        answer.append(temp)
    if len(answer) == 0:
        answer.append("EMPTY")
    return answer