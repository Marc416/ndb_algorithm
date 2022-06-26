import copy
import sys
from collections import deque


def virus_queue(graph: list) -> deque:
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 2:
                queue.append((i, j))
    return queue


def make_virus_spread_bfs(copy_graph: list) -> list:
    virus_queues = virus_queue(copy_graph)

    # 바이러스가 퍼져나간다
    while virus_queues:
        x, y = virus_queues.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 경계일 경우
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if copy_graph[nx][ny] == 0:
                copy_graph[nx][ny] = 2
                virus_queues.append((nx, ny))
    return copy_graph


def count_safe_area(virus_spread_graph: list):
    cnt = 0
    for i in range(n):
        for j in range(m):
            if virus_spread_graph[i][j] == 0:
                cnt += 1
    return cnt


def make_wall(cnt):
    global answer
    if cnt == 3:
        copy_graph = copy.deepcopy(graph)
        # 바이러스 증식시키기
        virus_spread_graph = make_virus_spread_bfs(copy_graph)
        # safe_area 크기 카운트
        temp_cnt = count_safe_area(virus_spread_graph)
        # 더 큰 safe_area 로 갱신
        answer = max(answer, temp_cnt)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                make_wall(cnt + 1)
                graph[i][j] = 0


si = sys.stdin.readline
n, m = map(int, si().rstrip().split())
graph = []
# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최종 답안
answer = 0

for i in range(n):
    graph.append(list(map(int, si().rstrip().split())))

make_wall(0)
print(answer)
