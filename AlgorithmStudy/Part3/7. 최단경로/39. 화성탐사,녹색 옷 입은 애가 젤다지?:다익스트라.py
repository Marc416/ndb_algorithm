# 답지를 보고 말음
import heapq
import sys

problem_num = 1
while True:
    n = int(sys.stdin.readline().rstrip())
    if n == 0:
        break
    distance = list([float('INF')] * n for _ in range(n))
    graph = []

    for _ in range(n):
        graph.append(list(map(int, sys.stdin.readline().rstrip().split())))
    x, y = 0, 0

    q = [(graph[x][y], x, y)]
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        current_dist, x, y = heapq.heappop(q)

        # 거리비교, 방문한곳인지 아닌지를 파악하기 위함
        if current_dist > distance[x][y]:
            continue

        # find next distance
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 밖인 경우 체크하지 않음
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            cost = current_dist + graph[nx][ny]
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(q, (cost, nx, ny))

    print(f'Problem {problem_num}: {distance[n - 1][n - 1]}')
    problem_num += 1
