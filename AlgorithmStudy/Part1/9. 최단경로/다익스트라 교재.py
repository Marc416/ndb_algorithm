import sys

""" 입력 """
# n, m = map(int, sys.stdin.readline())
n, m = 6, 11
# 시작노드 고정
start = 1
# 최단 거리를 찾는 것이므로 목적지 노드의 default 거리를 최대로 잡고 더 작은 것을 비교하기
distance = [float('inf')] * (n + 1)

visited = [0] * (n + 1)

graph = [[] for _ in range(n)]
input_data = [
    [1, 2, 2],
    [1, 3, 5],
    [1, 4, 1],
    [2, 3, 3],
    [2, 4, 2],
    [3, 2, 3],
    [3, 6, 5],
    [4, 3, 3],
    [4, 5, 1],
    [5, 3, 1],
    [5, 6, 2],
]

graph = list([] for _ in range(n + 1))


def init_data():
    for start, des, dist in input_data:
        graph[start].append((des, dist))


# 가장 최저 거리의 노드를 찾는 이유는 무엇일까
#  왜 처음 값들을 먼저 세팅시킬까
#  왜 n-1 번만 돌고 확인을 끝내는 것일까
def get_samllest_node():
    min_value = float('inf')
    index = 0
    for i in range(1, n + 1):
        #
        if distance[i] < min_value and visited[i] == 0:
            min_value = distance[i]
            index = i
    return index


def dikstra(start: int):
    distance[start] = 0
    visited[start] = 1
    for des, dist in graph[start]:
        distance[des] = dist
    for i in range(n - 1):
        # 전체 노드를 계속 탐색해서 가장 짧은 거리의 노드를 찾는다.
        now = get_samllest_node()
        visited[now] = True
        for j_des, j_dist in graph[now]:
            # 이전의 거리
            cost = distance[now] + j_dist
            # 새로 탐색한 거리
            if cost < distance[j_des]:
                distance[j_des] = cost

    pass


init_data()
dikstra(start=start)
print(distance)
# print(distance)
