import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
start = max(arr)
end = sum(arr)

while start <= end:
    mid = int((start+end)/2)
    total = 0 #레슨합
    count = 0 #현재 블루레이 개수
    for i in range(n):
        if total + arr[i] > mid: #현재 레슨시간 + total이 mid보다 크면
            count += 1 #블루레이 개수 추가
            total = 0 #새 블루레이로 교체하기 위해 total 0으로 초기화
        total += arr[i] #현재 레슨시간 더하기

    if total != 0: #0이 아니면 새 블루레이 필요
        count += 1
    if count > m: #블루레이 개수가 m보다 크면
        start = mid + 1
    else:
        end = mid - 1
print(start)