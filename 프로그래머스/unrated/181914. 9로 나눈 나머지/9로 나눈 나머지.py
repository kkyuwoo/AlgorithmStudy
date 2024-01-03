def solution(number):
    answer = 0
    total = 0
    for i in number:
        total += int(i)
    answer = total%9
    return answer