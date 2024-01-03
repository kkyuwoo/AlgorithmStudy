def solution(myString):
    answer = []
    temp = list(myString.split('x'))
    for i in temp:
        if i != "":
            answer.append(i)
    answer.sort()
    return answer