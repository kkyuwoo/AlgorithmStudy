def solution(my_string, s, e):
    answer = ''
    my_string = list(my_string)
    for i in range(s, s+(e-s)//2+1):
        temp = my_string[i]
        my_string[i] = my_string[s+e-i]
        my_string[s+e-i] = temp
    for i in my_string:
        answer += i
    return answer