import sys

n = int(sys.stdin.readline().rstrip())
x_default = []
y_default = []
z_default = []
for i in range(n):
    x, y, z = map(int, sys.stdin.readline().rstrip().split())
    x_default.append((x, i))
    y_default.append((y, i))
    z_default.append((z, i))

# # x,y,z 기준으로 오름차순 정렬
x_default.sort()
y_default.sort()
z_default.sort()

edges = []
# 간선 수(n-1)개를 계산 후 정렬
for i in range(n - 1):
    # x,y,z 좌표를 기준일 때의 노드간 길이 데이터 (cost,출발지,도착지)
    # 오름 차순 정렬을 해놨기 때문에 5-4,4-3,3-2,2-1 의 노드길이만 비교하면됨. 5-1,5-2 이런 비교를 하지 않아도 됨.
    # x 좌표
    edges.append((abs(x_default[i + 1][0] - x_default[i][0]), x_default[i][1], x_default[i + 1][1]))
    # y 좌표
    edges.append((abs(y_default[i + 1][0] - y_default[i][0]), y_default[i][1], y_default[i + 1][1]))
    # z 좌표
    edges.append((abs(z_default[i + 1][0] - z_default[i][0]), z_default[i][1], z_default[i + 1][1]))

# x,y,z기준으로 간선 리스트를 만드는 것이 모든 노드에 대한 리스트를 만드는 메모리보다 적게 쓰임
# 모든 간선 데이터 만들기 : n! 개
# x,y,z 의 간선 데이터 만들기 : n * 3 개
# 간선의 양이많아질 수록 팩토리얼의 결과값은 커지게됨 그래서 앞서 만든 로직은 메모리초과가 뜸.

# 간선들의 모음을 다시 정렬
edges.sort()

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
for edge in edges:
    cost, a, b = edge
    if count == n:
        break
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        res += cost
        count += 1

print(res)
