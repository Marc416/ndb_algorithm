import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# Set parent
parent = [0] * (n + 1)
for i in range(1, n + 1):
    parent[i] = i
# Get Edges data
edges = []
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2])


def find_parent(parent: list, node: int):
    if parent[node] != node:
        parent[node] = find_parent(parent, parent[node])

    return parent[node]


def union_parent(parent: list, a_node: int, b_node: int):
    a = find_parent(parent, a_node)
    b = find_parent(parent, b_node)
    if a == b:
        pass
    elif a < b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]


result = 0

for a, b, cost in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost
print(result)
