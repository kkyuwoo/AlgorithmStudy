import sys
n = int(sys.stdin.readline())
n_arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
m_arr = list(map(int, sys.stdin.readline().split()))
n_arr.sort()
for i in m_arr:
    left = 0
    right = n - 1
    check = 0
    while left <= right:
        mid = (left+right)//2
        if n_arr[mid] == i:
            check = 1
            print(1)
            break
        elif i > n_arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if check == 0:
        print(0)