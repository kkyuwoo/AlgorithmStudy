def solution(myString):
    answer = []
    count = 0
    for i in range(len(myString)):
        if myString[i] == 'x':
            answer.append(count)
            count = 0
        else:
            count += 1
    answer.append(count)
    return answer