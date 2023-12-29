n = int(input())
array = list(map(int, input().split()))
x = int(input())
array.sort()

start_index = 0
end_index = n-1
answer = 0

while start_index < end_index:
    temp = array[start_index] + array[end_index]
    if temp == x:
        answer += 1
        start_index += 1
    elif temp < x:
        start_index += 1
    else:
        end_index -= 1

print(answer)