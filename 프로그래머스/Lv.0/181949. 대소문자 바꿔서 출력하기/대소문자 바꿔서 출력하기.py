str = list(input())
for i in range(len(str)):
    if str[i] == str[i].upper():
        str[i] = str[i].lower()
    else:
        str[i] = str[i].upper()

result = ''
for i in str:
    result += i
print(result)