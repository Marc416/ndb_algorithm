from sys import stdin

v, e = 6, 4
data = [(1, 4), (2, 3), (2, 4), (5, 6)]
parent = [0] * (v + 1)

n, m = map(int, stdin.readline().split())
data = []
for i in range(m + 1):
    data.append(map(int, stdin.readline().split()))


def find_parent(parent: list, node: int):
    if parent[node] != node:
        # return find_parent(parent, parent[node])
        # 개선
        parent[node] = find_parent(parent, parent[node])
    # parent와 node가 같을 경우
    return parent[node]


def union_parent(parent: list, now_node: int, now_node_parent: int):
    a = find_parent(parent, now_node)
    b = find_parent(parent, now_node_parent)
    print(f'b:{b},a:{a}')
    if a == b:
        pass
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# 노드의 parent 자기 자신으로 설정
for i in range(1, v + 1):
    parent[i] = i

for now_node, now_node_parent in data:
    union_parent(parent, now_node, now_node_parent)
    print(f'now_node:{now_node}, now_node_parent:{now_node_parent}')
    print(parent[1:])

# 각원소가 속한 내용출력
for i in range(1, v + 1):
    print(find_parent(parent, i), end=' ')
print()

# 부모테이블 내역 출력
print(f'res : {parent[1:]}')
