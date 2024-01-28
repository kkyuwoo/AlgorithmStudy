def solution(n):
    answer = 0
    A = [0] * (n+1)
    
    for i in range(2, n+1):
        A[i] = i
        
    for i in range(2, int(n**0.5) + 1):
        if A[i] == 0:
            continue
        for j in range(i+i, (n+1), i):
            A[j] = 0
    
    for i in A:
        if i != 0:
            answer += 1
    return answer