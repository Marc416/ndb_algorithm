import heapq
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = list([] for _ in range(n))
for i in range(n):
    source = list(map(int, sys.stdin.readline().rstrip().split()))
    graph[i] = source

q = list(map(int, sys.stdin.readline().rstrip().split()))

while q:
    start = heapq.heappop(q)
    next_city = []
    # 갈 수 있는 도시 찾기
    for i in range(n):
        if graph[start][i] == 1:
            # 갈 수 있는 도시 대입
            next_city.append(i)

    if not next_city:
        continue
