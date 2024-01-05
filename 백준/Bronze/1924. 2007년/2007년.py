x, y = map(int, input().split())
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 0
if x > 1:
    for i in range(x-1):
        day += month[i]

day += y
if day % 7 == 1:
    print("MON")
elif day % 7 == 2:
    print("TUE")
elif day % 7 == 3:
    print("WED")
elif day % 7 == 4:
    print("THU")
elif day % 7 == 5:
    print("FRI")
elif day % 7 == 6:
    print("SAT")
else:
    print("SUN")