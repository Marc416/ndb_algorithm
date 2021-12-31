# 입력받은 데이터
from collections import deque

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

def bfs(graph, node, visited):
    # Init queue 생성
    queue = deque()
    # 처음 탐색할 node를 queue에 삽입
    queue.append(node)
    visited[node] = True

    # queue에 들어 있는 노드들의 인접한 곳들을 탐색한다.
    while queue:
        selected_node = queue.popleft()
        print(selected_node, end= " ")
        for i in graph[selected_node]:
            if visited[i]:
                continue
            else:
                # 탐색한 노드를 큐에 등록하고 등록한 큐의 인접한 노드들은 나중에 찾기로 약속
                queue.append(i)
                # 탐색한 노드를 방분기록지에 기록
                visited[i] = True

bfs(graph, 1, visited)