import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

count = 0
start_index = 0
end_index = n-1

while start_index < end_index:
    if num_list[start_index] + num_list[end_index] > m:
        end_index -= 1
    elif num_list[start_index] + num_list[end_index] < m:
        start_index += 1
    else:
        start_index += 1
        end_index -= 1
        count += 1

print(count)