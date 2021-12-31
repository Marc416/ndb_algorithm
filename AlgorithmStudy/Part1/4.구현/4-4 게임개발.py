n, m = 4, 4
x, y, direction = 1, 1, 0
game_map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
# n, m = map(int, input().split())
# x, y, d = map(int, input().split())
# game_map = list(list(map(int, input().split())) for _ in range(m))

went = ()
current_pos = {'xy': (x, y), 'dir': direction}


def get_left_pos(pos):
    validate_pos = pos['xy']
    match pos['dir']:
        # 북
        case 0:
            return {'xy': (validate_pos[0], validate_pos[1] + 1), 'dir': pos['dir']}
        # 동
        case 1:
            return {'xy': (validate_pos[0] + 1, validate_pos[1]), 'dir': pos['dir']}
        # 남
        case 2:
            return {'xy': (validate_pos[0], validate_pos[1] - 1), 'dir': pos['dir']}
        # 서
        case 3:
            return {'xy': (validate_pos[0] - 1, validate_pos[1] + 1), 'dir': pos['dir']}


def get_back_pos(pos):
    # 뒤가 바다인경우 움직이지 않는 것도 추가
    validate_pos = pos['xy']
    match pos['dir']:
        # 북
        case 0:
            back_pos = (validate_pos[0], validate_pos[1] - 1)
            # 뒤가 바다라면 움직이지 않는다.
            if game_map(back_pos) == 1:
                return current_pos
            return {'xy': back_pos, 'dir': pos['dir']}
        # 동
        case 1:
            back_pos = (validate_pos[0] - 1, validate_pos[1])
            # 뒤가 바다라면 움직이지 않는다.
            if game_map(back_pos) == 1:
                return current_pos
            return {'xy': back_pos, 'dir': pos['dir']}
        # 남
        case 2:
            back_pos = (validate_pos[0], validate_pos[1] + 1)
            # 뒤가 바다라면 움직이지 않는다.
            if game_map(back_pos) == 1:
                return current_pos
            return {'xy': back_pos, 'dir': pos['dir']}
        # 서
        case 3:
            back_pos = (validate_pos[0] + 1, validate_pos[1])
            # 뒤가 바다라면 움직이지 않는다.
            if game_map(back_pos) == 1:
                return current_pos
            return {'xy': back_pos, 'dir': pos['dir']}

    return current_pos


def turn_clock_reverse(current_direction):
    if current_direction == 3:
        return 0
    else:
        return current_direction + 1


# Used in 'validate_4direction_is_not_available'
def already_went_or_see(pos_xy):
    if game_map[pos_xy] == 1 or pos_xy in went:
        return True
    else:
        return False


# 주변 4방향이 보두 불가능한지 확인
def validate_4direction_is_not_available(pos):
    cnt = 0
    # 4 방향 확인
    for direction in range(4):
        each_pos = {'xy': pos['xy'], 'dir': direction}
        temp = get_left_pos(each_pos)
        if already_went_or_see(temp['xy']):
            cnt += 1

    if cnt > 3:
        return True
    else:
        return False


while True:
    left_pos_dir = get_left_pos(current_pos)
    temp_pose = left_pos_dir['xy']
    # 1. 현재위치에서 왼쪽에 있는 블럭이 육지이거나, 한번도 오지 않았던 곳이라면 왼쪽 블럭으로 간다.
    if game_map[temp_pose] == 0 or temp_pose not in went:
        current_pos = temp_pose
        went.append(current_pos['xy'])
        # 왼쪽이 이미 가본칸이라면 방향만 반시계방향으로 돌린다.
        next_temp_pose = get_left_pos(temp_pos)
        if game_map[next_temp_pose['xy']] == 1 or next_temp_pose['xy'] in went:
            current_pos['dir'] = turn_clock_reverse(current_pos['dir'])
        continue

    # 2. 동서남북 모두 가본 곳 또는 바다일 경우 한칸 뒤로간다.
    if validate_4direction_is_not_available(current_pos):
        temp_pos = get_back_pos(current_pos)
        # 만약 뒤가 바다라 갈 수 없다면 게임을 멈춘다.
        if current_pos == temp_pos:
            break
        else:
            current_pos = temp_pos
