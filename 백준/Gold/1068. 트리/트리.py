import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n)]
answer = 0
p = list(map(int, input().split())) #입력 데이터

for i in range(n):
    if p[i] != -1: #루트 노드가 아니면
        tree[i].append(p[i]) #tree 인접 리스트에 트리 데이터 저장
        tree[p[i]].append(i)
    else:
        root = i #루트 노드값 저장


def DFS(num):
    global answer
    visited[num] = True
    cNode = 0 #자식 노드 개수
    for i in tree[num]:
        if not visited[i] and i != deleteNode:
            cNode += 1
            DFS(i)
    if cNode == 0: #자식 노드 개수가 0이면 리프 노드 + 1
        answer += 1


deleteNode = int(input())

if deleteNode == root:
    print(0)
else:
    DFS(root)
    print(answer)
