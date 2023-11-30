import sys
n = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))
num_list.sort()

count = 0

for i in range(n):
    m = num_list[i]
    start_index = 0
    end_index = n-1

    while start_index < end_index:
        if num_list[start_index] + num_list[end_index] == m:
            if start_index != i and end_index != i:
                count += 1
                break
            elif start_index == i:
                start_index += 1
            elif end_index == i:
                end_index -= 1
        elif num_list[start_index] + num_list[end_index] < m:
            start_index += 1
        else:
            end_index -= 1

print(count)