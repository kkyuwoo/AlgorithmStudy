arr = list(input())
for i in range(0, len(arr), 10):
    for j in arr[i:i+10]:
        print(j, end='')
    print()