import re
def solution(babbling):
    answer = 0
    for char in babbling:
        if re.match(r"^(aya|ye|woo|ma)+$", char):
                answer += 1
    return answer