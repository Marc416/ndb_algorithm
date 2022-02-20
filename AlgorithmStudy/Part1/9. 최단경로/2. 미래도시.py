n, m = 5, 7
data = [(1, 2), (1, 3), (1, 4), (2, 4), (3, 4), (4, 5)]
x, k = 4, 5

# n, m = 4, 2
# data = [(1, 3), (2, 4)]
# x, k = 3, 4

graph = list([float('inf')] * (n + 1) for _ in range(n + 1))


def init_graph_self_value(node_count: int):
    # 자기 자신 노드 거리 -> 0
    for i in range(1, node_count + 1):
        graph[i][i] = 0
    # 연결된 노드 거리 입력 (거리는 1)
    for start, end in data:
        graph[start][end] = 1
        graph[end][start] = 1


def floyd_warshall(node_count: int):
    # 각 노드를 K라 가정할 때(거쳐가야 하는 도시 노드)
    for k in range(1, n + 1):
        # Start node
        for a in range(1, n + 1):
            if k == a:
                continue
            # End node
            for b in range(1, n + 1):
                if k == b:
                    continue
                graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


def cal_distance(ak: int, kb: int) -> int:
    if ak + kb >= float('inf'):
        return -1
    else:
        return ak + kb


init_graph_self_value(n)
floyd_warshall(n)

for source in graph:
    print(source)
print(cal_distance(ak=graph[1][k], kb=graph[k][x]))
