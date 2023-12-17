import sys

n = int(input())
tree = {}
for i in range(n):
    node, left, right = sys.stdin.readline().split()
    tree[node] = [left, right]


def preOrder(now):  # 전위 순회
    if now == '.':
        return
    print(now, end='')  # 루트
    preOrder(tree[now][0])  # 왼
    preOrder(tree[now][1])  # 오


def inOrder(now):  # 중위 순회
    if now == '.':
        return
    inOrder(tree[now][0])  # 왼
    print(now, end='')  # 루트
    inOrder(tree[now][1])  # 오


def postOrder(now):  # 후위 순회
    if now == '.':
        return
    postOrder(tree[now][0])  # 왼
    postOrder(tree[now][1])  # 오
    print(now, end='')  # 루트


preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
