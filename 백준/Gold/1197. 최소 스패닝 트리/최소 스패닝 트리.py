import sys
from queue import PriorityQueue

v, e = map(int, input().split())
q = PriorityQueue()
parent = [0] * (v + 1)

for i in range(v + 1):
    parent[i] = i

for i in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    q.put((c, a, b))  # 우선순위 큐이므로 자동 정렬(오름차순 정렬). 가중치를 기준으로 정렬해야 하므로 가중치를 제일 앞에 놓음


def find(m):
    if m == parent[m]:
        return m
    else:
        parent[m] = find(parent[m])
        return parent[m]


def union(m, n):
    m = find(m)
    n = find(n)
    if m != n:
        parent[n] = m #두 원소의 대표 노드끼리 연결

#MST 실행
useEdge = 0 #사용에지
result = 0

while useEdge < v - 1: #연결한 에지의 개수가 노드 수-1이 될 때까지
    w, s, e = q.get() #에지 정보 가져오기
    if find(s) != find(e): #에지 시작점과 끝점의 부모 노드가 다르면, 연결해도 사이클이 생기지 않으면
        union(s, e) #union 연산 수행
        result += w
        useEdge += 1 #연결 에지 개수 + 1

print(result)
