import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())

# 인접행렬 초기화 (INF)
graph = list([float('INF')] * (n + 1) for _ in range(n + 1))
# 시작 지점과 도착지점이 같은 경우 비용 0으로
for i in range(n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    # 시작 도시와 도착도시가 같은 경우가 없다하였으므로 따로 로직을 더 만들지 않아도 된다.
    # graph[a][b] = c
    # 하지만 위 조건이 없을 경우 비교해서 더 작은 값을 넣어주도록 하자.
    if graph[a][b] > c:
        graph[a][b] = c

print('prev graph')
for i in range(n + 1):
    print(graph[i])

print('res graph')
for v in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            if graph[s][e] > graph[s][v] + graph[v][e]:
                graph[s][e] = graph[s][v] + graph[v][e]

# RESULT
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == float('INF'):
            print(0, end=' ')
        else:
            print(graph[a][b], end=' ')
    print()
