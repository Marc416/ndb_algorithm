n, m = 6, 11
start = 1
di = [9999] * (n + 1)
di[start] = 0
# graph = [[] for _ in range(m)]
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
