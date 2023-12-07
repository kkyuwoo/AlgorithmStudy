answer = 0
A = list(map(str, input().split("-")))

for i in range(len(A)):
    plus = str(A[i]).split("+")
    temp = 0
    for j in plus:
        temp += int(j)
    if i == 0:
        answer += temp
    else:
        answer -= temp

print(answer)