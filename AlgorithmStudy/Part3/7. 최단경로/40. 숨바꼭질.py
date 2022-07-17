import heapq
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

graph = list([] for _ in range(n + 1))

distance = [float('INF')] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))

start = 1
q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    print(graph[i][1:])
#
# q = [graph[1]]
# while q:
#     node_list = heapq.heappop(q)
#
#     if not node_list:
#         continue
#
#     for node in node_list:
#         dist[node] += 1
#         if not graph[node]:
#             continue
#         heapq.heappush(q, graph[node])
#
# print(dist)
