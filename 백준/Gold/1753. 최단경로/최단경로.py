import sys
from queue import PriorityQueue

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
distance = [sys.maxsize] * (v + 1) #충분히 큰 수로 초기화
array = [[] for _ in range(v + 1)] # 에지 데이터 저장 인접 리스트
visited = [False] * (v + 1) #방문 여부 저장 리스트
q = PriorityQueue()

for i in range(e):
    w, y, z = map(int, sys.stdin.readline().split())
    array[w].append((y, z))

q.put((0, k)) #출발 노드는 우선순위 큐에 넣고 시작
distance[k] = 0 #거리 리스트에 출발 노드의 값을 0으로 설정
while q.qsize() > 0:
    current = q.get() #우선순위 큐에서 노드 가져오기
    c_v = current[1]
    if visited[c_v]:
        continue
    visited[c_v] = True
    for tmp in array[c_v]: #현재 선택 노드의 에지 개수
        nex = tmp[0] #연결 노드
        value = tmp[1] #가중치
        if distance[nex] > distance[c_v] + value: #연결 노드 최단 거리 > 현재 선택 노드 최단 거리 + 가중치
            distance[nex] = distance[c_v] + value #최소 거리로 업데이트
            q.put((distance[nex], nex)) #가중치가 정렬 기준이므로 순서를 가중치, 목표 노드 순으로 우선순위 큐 설정

for i in range(1, v + 1):
    if visited[i]:
        print(distance[i])
    else:
        print("INF")
