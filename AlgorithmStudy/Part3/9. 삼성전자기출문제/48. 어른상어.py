import sys


def init_map():
    for i in range(n):
        for j in range(n):
            shark_number = current_shark_array[i][j]
            if shark_number > 0:
                # 처음부터 중복된 상어는 없다고 했으므로 아래와같이 세팅 가능
                # (상어번호, 현재상어 방향) -> 시간은 4 로 냄새를 기록 하는 리스트에 자동 저장
                # dynamic[i][j] = (shark_number, shark_current_direction[shark_number])
                # 현재 상어 위치를 기록
                current_shark_pos[shark_number] = (i, j)
                current_shark_array[i][j] = (shark_number, current_shark_direction[shark_number])
                shark_smell_map[i][j] = (shark_number, k)
            else:
                # 상어가 없으면 (0,0,0) 으로 변경
                current_shark_array[i][j] = (0, 0)


def remove_past_pos(px: int, py: int):
    current_shark_array[px][py] = (0, 0)


def move_shark(_shark_numb: int) -> tuple:
    """ 움직인 후 상어번호, x값, y값 반환"""
    _current_direction = current_shark_direction[_shark_numb]
    _current_pos_x = current_shark_pos[_shark_numb][0]
    _current_pos_y = current_shark_pos[_shark_numb][1]
    # 현재 상어방향에 따른 다읍 방향 탐색 계획 리스트를 가져오기 (ex. 3번 상어의 현재 방향이 '위' 일때 계획 가져오기)
    _next_direction_list = shark_moving_logic[_shark_numb][_current_direction]

    temp_x = None
    temp_y = None
    temp_direction = None
    for direction in _next_direction_list:
        nx = _current_pos_x + get_pos(direction)[0]
        ny = _current_pos_y + get_pos(direction)[1]

        # 경계
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        # 냄새가 없으면 정착
        if shark_smell_map[nx][ny] == (0, 0):
            # array 의 과거 위치 삭제
            remove_past_pos(px=_current_pos_x, py=_current_pos_y)
            # list 에서 현재위치 변경
            current_shark_pos[_shark_numb] = (nx, ny)
            # 상어의 현재방향 변경
            current_shark_direction[_shark_numb] = direction
            # next smell map 갱신
            shark_smell_map[nx][ny] = (_shark_numb, k)
            return nx, ny

        # 자신의 냄새일 경우 저장
        if shark_smell_map[nx][ny][0] == _shark_numb:
            temp_direction = direction
            temp_x = nx
            temp_y = ny
            continue

    if temp_x is None or temp_y is None:
        raise

    # 모두 냄새가 있을 경우 자신의 냄새가 나는 방향으로 변경
    # array 의 과거 위치 삭제
    remove_past_pos(px=_current_pos_x, py=_current_pos_y)
    # list 에서 현재위치 변경
    current_shark_pos[_shark_numb] = (temp_x, temp_y)
    # 상어의 현재방향 변경
    current_shark_direction[_shark_numb] = temp_direction
    # next smell map 갱신
    shark_smell_map[temp_x][temp_y] = (_shark_numb, k)

    return temp_x, temp_y


def get_pos(pos: int) -> tuple:
    if pos == 1:
        return dx[0], dy[0]
    elif pos == 2:
        return dx[1], dy[1]
    elif pos == 3:
        return dx[2], dy[2]
    elif pos == 4:
        return dx[3], dy[3]


def update_smell():
    for i in range(n):
        for j in range(n):
            _shark_numb, _count = shark_smell_map[i][j]
            if _shark_numb > 0 and (0 < _count <= k):
                if _count - 1 > 0:
                    shark_smell_map[i][j] = (_shark_numb, _count - 1)
                else:
                    shark_smell_map[i][j] = (0, 0)


si = sys.stdin.readline
# n : 맵크기, m : 상어 수, k : 냄새 지속시간
n, m, k = map(int, si().split())
current_shark_array = []
for _ in range(n):
    current_shark_array.append(list(map(int, si().split())))

# 현재 상어의 방향입력 (상어가 격자로부터 나오게되면 -1)
current_shark_direction = [0]  # 상어는 1번부터이므로 0번 인덱스는 0으로
current_shark_direction.extend(list(map(int, si().split())))

# 1:위, 2:아래, 3:왼쪽, 4:오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 인덱스번호를 상어번호로 쓰기 위해 0을 미리 넣음
shark_moving_logic = [0]
for i in range(m):
    up_rule = list(map(int, si().split()))
    down_rule = list(map(int, si().split()))
    left_rule = list(map(int, si().split()))
    right_rule = list(map(int, si().split()))
    # 상어 현재의 방향에 따른 다음 탐색할 방향계획을 입력받기
    # 1, 2, 3, 4 번 방향 순서대로 상어 Index에 맞춰서 입력 (방향 순서가 1부터 시작하므로 0을 미리 입력)
    shark_moving_logic.append([0, up_rule, down_rule, left_rule, right_rule])

# 현재 상어 위치 (-1,-1) 이라면 상어는 존재하지 않는다.
current_shark_pos = list((-1, -1,) for _ in range(m + 1))
# 냄새 흔적 지도
shark_smell_map = list([(0, 0)] * n for _ in range(n))  # (상어번호, 냄새 시간)

# 맵 Init
init_map()

# 결과로 제출할 상어의 수
count_shark = m

second = 0


def remove_shark_in_dynamic(temp_map: list):
    global count_shark
    for i in range(n):
        for j in range(n):
            if len(temp_map[i][j]) >= 2:  # 두개이상 잘들어오는지 체크
                live_shark = min(temp_map[i][j])
                for s in temp_map[i][j]:
                    if s == live_shark:
                        continue
                    else:
                        # 가장 작은 상어가 아닌 경우 out
                        current_shark_pos[s] = (-1, -1)
                        current_shark_array[i][j] == (0, 0)
                        count_shark -= 1


while True:
    # 1,000초가 넘어도 다른 상어가 격자에 남아 있으면 -1을 출력
    if second > 1000:
        break

    # 상어수가 1마리이면 종료
    if count_shark <= 1:
        break

    # 1. 냄새기록 업데이트
    update_smell()

    # 3번을 위한 임시 리스트 ; 1초동안 탐색을 마치고 같은 칸에 상어가 2마리이상 시 제거하기 위함
    merge_shark = list([[] for _ in range(n)] for _ in range(n))

    # 1. 상어를 순서대로 한마리씩 움직이기 (1번상어부터)
    for _shark_idx, _pos in enumerate(current_shark_pos[1:], start=1):
        # 상어가 격자 밖으로 나간경우 다음 상어 이동
        if _pos == (-1, -1):
            continue

        # 2. 상어 이동
        # 경쟁
        x, y = move_shark(_shark_numb=_shark_idx)
        if merge_shark[x][y] :
            _shark_numb = min(merge_shark[x][y][0], _shark_idx)
            _remove_shark_numb = max(merge_shark[x][y][0], _shark_idx)
            merge_shark[x][y] = (_shark_numb, current_shark_direction[_shark_numb])
            current_shark_pos[_remove_shark_numb] = (-1, -1)
            current_shark_direction[_remove_shark_numb] = 0
        # 비어있을 때
        else:
            merge_shark[x][y] = (_shark_idx, current_shark_direction[_shark_idx])
    # 3. 상어가 겹쳐있으면 삭제 (현재위치 갱신)
    current_shark_array = merge_shark
    for ps in merge_shark:
        print(ps)
    print()
    for a in shark_smell_map:
        print(a)
    print()

    second += 1

# 결과 출력
if count_shark == 1:
    print(count_shark)
else:
    print(-1)
