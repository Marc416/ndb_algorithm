import heapq
import sys

n = int(sys.stdin.readline().rstrip())
dynamic = []
for _ in range(n):
    temp_list = list(map(int, sys.stdin.readline().rstrip().split()))
    dynamic.append(temp_list)

q = []
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

    # 특별한 룰은 아니지만 오름차순으로 parent 를 설정해줌
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


res = 0
count = 0
while q:
    cost, a, b = heapq.heappop(q)
    if count == n:
        break
    if find_parent(parent, a) != find_parent(parent, b):
        count += 1
        union_parent(parent, a, b)
        res += cost

print(res)
