import sys

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, -1, 1]

n, m, k = map(int, input().split())

# shark_array : 상어위치를 나타내는 인접행렬
# shark_list : 상어의 위치를 나타내는 인접리스트
shark_array, shark_list = [], [[] for _ in range(m)]
for i in range(n):
    # 상어별 위치 입력
    shark_array.append(list(map(int, input().split())))
    for j in range(n):
        # 상어가 있으면
        if shark_array[i][j]:
            # 상어의 인접리스트 갱신
            # 상어의 인덱스에 현재 상어의 위치를 기록
            shark_list[shark_array[i][j] - 1].extend([i, j])
            # (상어 넘버, 남은 초) 로 인접행렬 형태 변경
            shark_array[i][j] = [shark_array[i][j], k]

# 현재 상어의 방향
direction = list(map(int, input().split()))
for i in range(m):
    # 상어의 인접리스트 형태 변경 [.., [x,y,direction] ...]
    shark_list[i].append(direction[i])

# 상어별 다음을 탐색할 방향 규칙
direction_rule = [[] for _ in range(m)]
# 1번 상어부터
idx = -1
for i in range(4 * m):
    # 상어별로 4개씩 입력
    if i % 4 == 0:
        idx += 1
    # 4 방향 규칙을 입력받기
    direction_rule[idx].append(list(map(int, input().split())))

second = 0
while True:
    second += 1
    # 1000초가 넘어가면 종료
    if second == 1001:
        print(-1)
        break

    # 중복된 위치의 상어를 제거하기위한 임시 array
    check = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(m):
        # 상어 인접리스트에 상어가 있다면 움직이기
        if shark_list[i] != 0:
            # flag : 상어가 이미 있는지를 보여줌
            x, y, direction, flag = shark_list[i][0], shark_list[i][1], shark_list[i][2], 0

            for j in range(4):
                # 상어의 다음 탐색 방향 찾기
                next_dir = direction_rule[i][direction - 1][j]
                nx, ny = x + dx[next_dir], y + dy[next_dir]

                # 다음 방향이 수족관 범위에 속하는지 검사
                if 0 <= nx < n and 0 <= ny < n:
                    # 상어가 없다면 탐색 종료
                    if shark_array[nx][ny] == 0:
                        flag = 1
                        break

            # 이미 위치에 상어가 있는 경우 nx, ny, next_dir 을 자신의 냄새가 있는 인접방향으로 변경
            if flag == 0:
                for j in range(4):
                    next_dir = direction_rule[i][direction - 1][j]
                    nx, ny = x + dx[next_dir], y + dy[next_dir]
                    if 0 <= nx < n and 0 <= ny < n:
                        if shark_array[nx][ny][0] == i + 1:  # 현재 for 문의 범위는 0번부터 시작하므로 i에 1을 더해준다
                            break

            # 중복된 상어 제거
            if check[nx][ny]:
                # 임시 array 에 상어가 있고 현재 이동중인 상어보다 작은지 확인
                if check[nx][ny] < i + 1:
                    shark_list[i] = 0
                else:
                    # 없어지는 상어인 경우 인접리스트 업데이트 ; [x,y,direction] -> 0
                    shark_list[check[nx][ny] - 1] = 0
            else:
                check[nx][ny] = i + 1
                # 현재 상어 위치를 갱신
                shark_list[i] = [nx, ny, next_dir]

    # 다음 위치로 이동한 상어냄새를 제외한 모든 냄새를 업데이트 ; -1 씩 카운트다운
    for i in range(n):
        for j in range(n):
            if shark_array[i][j]:
                shark_array[i][j][1] -= 1
                if shark_array[i][j][1] == 0:
                    shark_array[i][j] = 0

    # 다음위치로 이동한 상어 냄새를 업데이트
    for i in range(m):
        if shark_list[i]:
            x, y = shark_list[i][0], shark_list[i][1]
            shark_array[x][y] = [i + 1, k]

    # 상어의 인접리스트 중 0 의 수가 m-1인경우 == 상어가 1마리인 경우
    if shark_list.count(0) == m - 1:
        print(second)
        break
