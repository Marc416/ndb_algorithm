import heapq
import sys

n = int(sys.stdin.readline().rstrip())
dynamic = []
for _ in range(n):
    temp_list = list(map(int, sys.stdin.readline().rstrip().split()))
    dynamic.append(temp_list)

q = []
# 모든 지점들에 대한 간선 데이터를 다이나믹으로 생성 -> 메모리 초과
for i in range(n - 1):
    for j in range(i + 1, n):
        xi, yi, zi = dynamic[i]
        xj, yj, zj = dynamic[j]
        ij_source = (min(abs(xi - xj), abs(yi - yj), abs(zi - zj)), i, j)
        heapq.heappush(q, ij_source)

parent = list(i for i in range(n))


def find_parent(parent: list, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


res = 0
count = 0
while q:
    cost, a, b = heapq.heappop(q)
    # 모든 노드를 연결 하면 순환문 탈출
    if count == n:
        break
    if find_parent(parent, a) != find_parent(parent, b):
        count += 1
        union_parent(parent, a, b)
        res += cost

print(res)
