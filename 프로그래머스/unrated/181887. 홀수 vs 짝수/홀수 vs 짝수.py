def solution(num_list):
    answer = 0
    odd_sum = 0
    even_sum = 0
    for i in range(0, len(num_list), 2):
        odd_sum += num_list[i]
    
    for i in range(1, len(num_list), 2):
        even_sum += num_list[i]
    
    if odd_sum > even_sum:
        answer = odd_sum
    else:
        answer = even_sum
    return answer