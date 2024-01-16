def solution(n):
    answer = [[0] * n for _ in range(n)]
    num = 1
    left, right, top, bottom = 0, n-1, 0, n-1
    
    while num <= n*n:
        #오른쪽
        for i in range(left, right+1):
            answer[top][i] = num
            num += 1
        top += 1
        
        #아래
        for i in range(top, bottom+1):
            answer[i][right] = num
            num += 1
        right -= 1
        
        #왼쪽
        for i in range(right, left-1, -1):
            answer[bottom][i] = num
            num += 1
        bottom -= 1
        
        #위
        for i in range(bottom, top-1, -1):
            answer[i][left] = num
            num += 1
        left += 1
        
    return answer