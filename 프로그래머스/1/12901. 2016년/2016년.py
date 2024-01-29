def solution(a, b):
    answer = ''
    days = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(a-1):
        total += months[i]
    total += b
    answer = days[total%7]
    return answer