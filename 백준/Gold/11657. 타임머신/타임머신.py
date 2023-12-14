import sys

n, m = map(int, input().split())
edges = []
distance = [sys.maxsize] * (n+1)

for i in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    edges.append((a, b, c))

distance[1] = 0 #거리 리스트에 출발 노드 0으로 초기화

for _ in range(n-1): #노드 개수-1 만큼 반복
    for a, b, c in edges: #에지 개수만큼 반복
        if distance[a] != sys.maxsize and distance[b] > distance[a] + c: #D[출발노드] != 무한대이며 D[종료 노드] > D[출발 노드] + 가중치일때
            distance[b] = distance[a] + c #D[종료노드] = D[출발 노드] + 가중치

mCycle = False

for a, b, c in edges:
    if distance[a] != sys.maxsize and distance[b] > distance[a] + c: #D[출발노드] != 무한대이며 D[종료 노드] > D[출발 노드] + 가중치일때(업데이트 가능하면)
        mCycle = True #음수 사이클 존재

if not mCycle:
    for i in range(2, n+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)