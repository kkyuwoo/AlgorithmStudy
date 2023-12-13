import sys
from queue import PriorityQueue

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
array = [[] for _ in range(n+1)]
visited = [False] * (n+1)
distance = [sys.maxsize] * (n+1)
q = PriorityQueue()

for i in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    array[start].append((end, cost))

s, e = map(int, (sys.stdin.readline().split()))

q.put((0, s))
distance[s] = 0

while q.qsize() > 0:
    nowNode = q.get()
    now = nowNode[1]
    if not visited[now]:
        visited[now] = True
        for i in array[now]:
            if not visited[i[0]] and distance[i[0]] > distance[now] + i[1]: #타깃 노드 방문 전 and 타깃 노드의 최단 거리 > 현재 선택 노드 최단 거리 + 비용:
                distance[i[0]] = distance[now] + i[1] # 타깃 노드 최단 거리 업데이트
                q.put((distance[i[0]], i[0])) #우선순위 큐에 타깃 노드 추가

print(distance[e])