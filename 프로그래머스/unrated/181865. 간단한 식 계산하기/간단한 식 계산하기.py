def solution(binomial):
    answer = 0
    array = list(binomial.split())
    if array[1] == '+':
        answer = int(array[0]) + int(array[2])
    elif array[1] == '-':
        answer = int(array[0]) - int(array[2])
    else:
        answer = int(array[0]) * int(array[2])
            
    return answer