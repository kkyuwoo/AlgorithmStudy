def solution(arr):
    answer = []
    array = [1, 2, 2**2, 2**3, 2**4, 2**5, 2**6, 2**7, 2**8, 2**9, 2**10]
    if len(arr) not in array:
        while len(arr) not in array:
            arr.append(0)
        answer = arr
    else:
        answer = arr
    return answer