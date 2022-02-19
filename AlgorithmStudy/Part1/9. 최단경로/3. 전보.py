import heapq

n, m, c = 3, 2, 1
data = [
    (1, 2, 4),
    (1, 3, 2)
]

graph = list([] for _ in range(n + 1))
distance = [float('inf')] * (n + 1)


def init_graph_with_data(data: list):
    for start, end, dist in data:
        graph[start].append((dist, end))


def dijkstra(start: int):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        # now 인덱스까지 갔을 때의 최소 거리를 작은 순서대로 pop
        dist, now = q.pop()

        # 기존의 거리가 더 작으면 continue (q에서 작은 것만 뽑으려 한 이유가 dist 비교로 아래의 for 문을 최소한으로 돌리기 위함.
        if distance[now] < dist:
            continue

        for next_dist, next in graph[now]:
            cost = dist + next_dist
            if cost < distance[next]:
                distance[next] = cost
                # 현재까지 탐색한 데이터 -> 다음 탐색을 위함
                heapq.heappush(q, (distance[next], next))


init_graph_with_data(data)
dijkstra(start=c)

# 메시지 전달한 도시 수
count = 0
# 모든 메시지를 전달하기 까지의 시간
max_time = 0

for i in distance:
    if i == float('inf'):
        continue
    if i == 0:
        continue
    count += 1
    max_time = max(max_time, i)

print(count, max_time)
