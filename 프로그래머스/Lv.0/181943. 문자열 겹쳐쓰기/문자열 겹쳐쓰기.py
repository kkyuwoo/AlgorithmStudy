def solution(my_string, overwrite_string, s):
    answer = ''
    my_string = list(my_string)
    my_string[s:s+len(overwrite_string)] = list(overwrite_string)
    for i in my_string:
        answer += i
    return answer