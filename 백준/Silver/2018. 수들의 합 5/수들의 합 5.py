import sys
n = int(sys.stdin.readline())
count = 1
start_index = 1
end_index = 1
total = 1
while end_index != n:
    if total == n:
        count += 1
        end_index += 1
        total += end_index
    elif total > n:
        total -= start_index
        start_index += 1
    else:
        end_index += 1
        total += end_index

print(count)