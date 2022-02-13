import sys

""" 입력 """
# n, m = map(int, sys.stdin.readline())
n, m = 6, 11
# 시작노드 고정
start = 1
# 최단 거리를 찾는 것이므로 목적지 노드의 default 거리를 최대로 잡고 더 작은 것을 비교하기
di = [float('inf')] * (n + 1)
# 시작 노드의 경로 이동 거리는 0
di[start] = 0

# graph = [list(map(int, input().split())) for _ in range(n)]
graph = [
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

for i in graph:
    # 이전 경로 거리
    pre_distance = di[i[1]]
    # 새로운 경로 거리
    new_distance = di[i[0]] + i[2]
    # 비교 (작은것 선택)
    di[i[1]] = min(pre_distance, new_distance)

print(di[1:])
