v, e = 7, 9
data = [(1, 2, 29), (1, 5, 75), (2, 3, 35), (2, 6, 34), (3, 4, 7), (4, 6, 23), (4, 7, 13), (5, 6, 53), (6, 7, 25)]
parent = [0] * (v + 1)
cycle = False


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

edges = data
# sort를 왜하는가? : 긴 간선을 가진 노드가 연결되게 됨.(싸이클이 있는 경우) -> 효율적인 간선연결이 안돼서 sort해야함.
edges.sort(key=lambda eg: eg[2])
result = 0

for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(parent)
print(result)
