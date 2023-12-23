A = [''] + list(input())
B = [''] + list(input())
array = [['' for _ in range(len(B))] for _ in range(len(A))]
for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            array[i][j] = array[i - 1][j - 1] + A[i]
        else:
            if len(array[i-1][j]) > len(array[i][j-1]):
                array[i][j] = array[i-1][j]
            else:
                array[i][j] = array[i][j-1]

result = array[-1][-1]
print(len(result))
print(result)