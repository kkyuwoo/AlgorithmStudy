x = int(input())
stick = 64
result = 0

while x > 0:
    if x >= stick:
        result += 1
        x -= stick
    else:
        stick = stick // 2

print(result)