import sys
from collections import deque

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, l, r = map(int, sys.stdin.readline().split())  # n*n, 인구차이 l명 이상, r명 이하

nation_map = list()
for _ in range(n):
    nation_map.append(list(map(int, sys.stdin.readline().split())))


def is_moving_bfs(i: int, j: int) -> bool:
    dq = deque()
    dq.append((i, j))
    visit[i][j] = True

    # 연합국가 리스트
    union = [(i, j)]

    # 인구이동을 하기 위해 첫번째 탐색국가 인구를 total_human_count 에 대입
    total_human_count = nation_map[i][j]

    # 1. 인접 국가를 탐색하면서 인구차이 l명 이상, r명 이하인 경우 연합 국가에 담기
    while dq:
        x, y = dq.popleft()

        # 4방향 인접 국가 탐색
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]

            # 국가 경계밖일 경우 Continue
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            # 이미 방문한 국가인 경우 Continue
            if visit[nx][ny]:
                continue

            # 인구차이 l명 이상, r명 이하인 경우, 연합 국가에 담기
            if l <= abs(nation_map[nx][ny] - nation_map[x][y]) <= r:
                union.append((nx, ny))

                # 조건에 모두 맞았을 때에만 방문처리
                # (A 국가와 C 국가간의 조건이 맞지 않더라도 B국가와 C국가의 조건이 맞을 수 있기 때문)
                visit[nx][ny] = True

                # 다음 탐색을 위해 탐색 큐에 append
                dq.append((nx, ny))
                total_human_count += nation_map[nx][ny]

    # 2. 연합 국가 간 인구 재분배
    # (연합의 인구수) / (연합을 이루고 있는 칸의 개수)
    for x, y in union:
        nation_map[x][y] = int(total_human_count / len(union))

    if len(union) > 1:
        return True
    else:
        return False


# 인구 이동이 발생하는 일수
moving_day_result = 0

while True:
    # 1. 인구 이동이 없을 때까지 반복
    visit = [[False] * n for _ in range(n)]
    flag = False  # 인구 이동 존재 유무 플래그

    # 2. nation_map (2차행열) 전체 탐색, 연합 진행
    # 전체 탐색 1번 = 1 day
    # 1 day 동안 flag 가 False 를 유지하는 경우 "인구이동 종료"
    for i in range(n):
        for j in range(n):
            # 방문을 하지 않은 국가
            if not visit[i][j]:
                # 연합의 발생 수 = 인구이동(True)
                if is_moving_bfs(i, j) is True:
                    flag = True

    # 3. 1 day 동안 flag 가 False 를 유지하는 경우 "인구이동 종료"
    if not flag:
        break

    moving_day_result += 1

print(moving_day_result)
