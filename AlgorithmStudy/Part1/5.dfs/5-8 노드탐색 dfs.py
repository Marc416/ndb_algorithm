# 입력받은 데이터
graph = [
    # 노드 0부터 데이터가 제시됨 ->노드 0은 없다 -> Null
    [],
    # 노드 1
    [2, 3, 8],
    # 노드 2
    [1, 7],
    # 노드 3
    [1, 4, 5],
    # 노드 4
    [3, 5],
    # 노드 5
    [3, 4],
    # 노드 6
    [7],
    # 노드 7
    [2, 6, 8],
    # 노드 8
    [1, 7]
]

# 가본곳을 Check 하는 방문기록지
visited = [0] * 9


def dfs(graph, node, visited):
    # 범위밖 데이터를 탐색하려고 하면 Return
    if node < 1 or node > 8:
        return

    # 이미 방문한 곳이라면 Return
    if visited[node] == 1:
        return

    # 처음 방문한 곳이라면 방문기록지에 등록
    visited[node] = 1
    print(node)

    # 방금 탐색한 노드와 인접한 노드들을 재귀문으로 탐색
    for i in graph[node]:
        dfs(graph, i, visited)


# 노드 1부터 탐색 : 주어진 데이터가 노드 1부터 주어지기 때문
dfs(graph, 1, visited)
