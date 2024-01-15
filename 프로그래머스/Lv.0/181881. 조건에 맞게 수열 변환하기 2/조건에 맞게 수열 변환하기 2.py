def solution(arr):
    answer = 0
    while True:
        new = []
        for i in arr:
            if i >= 50 and i % 2 == 0:
                new.append(i//2)
            elif i < 50 and i % 2 != 0:
                new.append(i*2+1)
            else:
                new.append(i)
                
        if new == arr:
            break
        else:
            arr = new
            answer += 1
                
    return answer