import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
visited = [False] * (n + 1)
tree = [[] for _ in range(n + 1)]
answer = [0] * (n + 1)

for _ in range(1, n): #tree 인접 리스트에 트리 데이터 저장
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def DFS(num): #현재노드
    visited[num] = True #현재 노드 방문 기록
    for i in tree[num]: #현재 노드의 연결 노드 중 미방문 노드
        if not visited[i]:
            answer[i] = num #미방문 노드의 부모 노드로 현재 노드 저장
            DFS(i)


DFS(1)

for i in range(2, n + 1):
    print(answer[i])
