def solution(n_str):
    answer = ''
    num = 0
    for i in range(len(n_str)):
        if n_str[i] != '0':
            num = i
            break
    answer = n_str[num:]
    return answer