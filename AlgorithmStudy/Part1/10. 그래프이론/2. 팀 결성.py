# n, m = 7, 8
# data = [
#     (0, 1, 3),
#     (1, 1, 7),
#     (0, 7, 6),
#     (1, 7, 1),
#     (0, 3, 7),
#     (0, 4, 2),
#     (0, 1, 1),
#     (1, 1, 1),
# ]
#
# parent = [0] * (n + 1)
# for i in range(n + 1):
#     parent[i] = i
#
# """ 👆 SET DATA """
#
#
# def find_parent(_parent: list, _node: int) -> int:
#     """ 노드의 parent node 찾기 : index와 parent node의 값이 같은 것 """
#     if _parent[_node] != _node:
#         _parent[_node] = find_parent(_parent, _parent[_node])
#     return _parent[_node]
#
#
# def union_parent(_parent: list, _now_node: int, _now_node_parent: int):
#     """ 연결된 노드 데이터를 비교하여 parent node의 값이 작은 노드로 합치기 """
#     _a = find_parent(_parent, _now_node)
#     _b = find_parent(_parent, _now_node_parent)
#     if _a < _b:
#         _parent[_b] = _a
#     else:
#         _parent[_a] = _b
#
#
# for cal, a, b in data:
#     # 팀합치기
#     if cal == 0:
#         union_parent(parent, a, b)
#     else:
#         if find_parent(parent, a) == find_parent(parent, b):
#             print('YES')
#         else:
#             print('NO')

import sys
sys.setrecursionlimit(10**6)
n, m = map(int, sys.stdin.readline().split())
parent = [0] * (n + 1)

for i in range(1, n + 1):
    parent[i] = i


def find_parent(parent: list, node: int):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])
    return parent[node]


def union_parent(parent: list, now_node: int, now_node_parent: int):
    a = find_parent(parent, now_node)
    b = find_parent(parent, now_node_parent)
    if a == b:
        pass
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


for _ in range(m):
    # 팀합치기
    cal, a, b = map(int, sys.stdin.readline().split())
    if cal == 0:
        union_parent(parent, a, b)
    else:
        if find_parent(parent, a) == find_parent(parent, b):
            print('YES')
        else:
            print('NO')
