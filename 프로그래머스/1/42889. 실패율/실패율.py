def solution(N, stages):
    answer = []
    stages_arr = [0] * 502
    arr = {}
    
    for i in range(len(stages)):
        stages_arr[stages[i]] += 1
    
    for i in range(1, N+1):
        total = sum(stages_arr[i:])
        now = stages_arr[i]
        if total != 0:
            arr[i] = (now/total)
        else:
            arr[i] = 0
            
    arr = sorted(arr.items(), key= lambda item:item[1], reverse=True)
    for key, value in arr:
        answer.append(key)
        
    return answer