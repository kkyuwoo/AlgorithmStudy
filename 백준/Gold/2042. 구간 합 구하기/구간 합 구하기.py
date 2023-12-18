import sys

n, m, k = map(int, input().split())
treeHeight = 0 #트리 높이
length = n #리프 노드 개수

while length != 0: #트리 높이 구하기
    length //= 2
    treeHeight += 1

treeSize = pow(2, treeHeight + 1)
leftNodeStartIndex = treeSize // 2 - 1 #리프 노드 시작 인덱스
tree = [0] * (treeSize + 1) #인덱스 트리 저장 리스트

for i in range(leftNodeStartIndex + 1, leftNodeStartIndex + n + 1): #tree 리스트의 리프 노드 영역에 데이터 입력
    tree[i] = int(sys.stdin.readline())

#인덱스 트리 생성 함수
def setTree(i):
    while i != 1: #인덱스가 루트가 아닐 때까지
        tree[i // 2] += tree[i] #부모 노드(인덱스/2)에 현재 index의 트리값 더하기
        i -= 1

#초기 트리 생성
setTree(treeSize - 1)

#값 변경 함수
def changeVal(index, value):
    diff = value - tree[index] #현재 노드의 값과 변경된 값의 차이
    while index > 0: #시작 인덱스가 0보다 클 때
        tree[index] = tree[index] + diff #시작 인덱스의 트리값에 diff 값을 더함
        index = index // 2

#구간 합 계산 함수
def getSum(s, e): #시작 인덱스, 종료 인덱스
    partSum = 0
    while s <= e:
        if s % 2 == 1: #start_index % 2 == 1일 때
            partSum += tree[s] #해당 노드의 값을 구간 합에 추가
            s += 1 #시작 인덱스 증가
        if e % 2 == 0: #end_index % 2 == 0일 때
            partSum += tree[e] #해당 노드의 값을 구간 합에 추가
            e -= 1 # 종료 인덱스 감소
        s = s // 2 #start_index depth 변경
        e = e // 2 #end_index depth 변경
    return partSum


for _ in range(m + k):
    question, s, e = map(int, sys.stdin.readline().split())
    if question == 1:
        changeVal(leftNodeStartIndex + s, e)
    elif question == 2:
        s = s + leftNodeStartIndex
        e = e + leftNodeStartIndex
        print(getSum(s, e))
