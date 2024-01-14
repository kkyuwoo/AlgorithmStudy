def solution(x1, x2, x3, x4):
    answer = True
    if not x1 and not x2:
        left = False
    else:
        left = True
    if not x3 and not x4:
        right = False
    else:
        right = True
    if left and right:
        answer = True
    else:
        answer = False
    return answer