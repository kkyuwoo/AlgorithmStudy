def solution(str_list):
    answer = []
    left = -1
    right = -1
    for i in range(len(str_list)):
        if str_list[i] == "r":
            right = i
            break
        elif str_list[i] == 'l':
            left = i
            break
    if left != -1:
        answer = str_list[:left]
    if right != -1:
        answer = str_list[right+1:]
    return answer