def solution(myString, pat):
    answer = ''
    arr = myString.split(pat)
    for i in range(len(arr)-1):
        answer += arr[i]
        answer += pat
    return answer