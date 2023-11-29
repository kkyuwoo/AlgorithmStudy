n = int(input())
score = list(map(int, input().split()))
total = 0
m = max(score)
for i in score:
    total += int(i)/m*100
print(total/n)