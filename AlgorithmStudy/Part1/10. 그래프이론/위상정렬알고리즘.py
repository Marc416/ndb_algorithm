# 우선순위 순서대로 일을 나열하는 알고리즘
from collections import deque

v, e = 7, 8
data = [(1, 2), (1, 5), (2, 3), (2, 6), (3, 4), (4, 7), (5, 6), (6, 4)]
indegree = [0] * (v + 1)
graph = [[] for int in range(v + 1)]
result = []

for a, b in data:
    graph[a].append(b)
    # 진입차수 1 증가 (b로 유입되는 간선)
    indegree[b] += 1


def topology_sort():
    q = deque()

    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # now node에서 갈라져나오는 node들의 우선순위에 따라 작업테스크에 넣을 수 있을 거 같음.
        for connected_node in graph[now]:
            indegree[connected_node] -= 1
            if indegree[connected_node] == 0:
                q.append(connected_node)


topology_sort()
print(result)
