# import sys
#
# # 보드의 크기 (보드만들기)
# n = int(sys.stdin.readline().rstrip())
# board = list([0] * n for _ in range(n))
# # 사과의 개수
# k = int(sys.stdin.readline().rstrip())
# # 사과의 위치
# for _ in range(k):
#     y, x = map(int, sys.stdin.readline().rstrip().split())
#     board[y][x] = 1
# # 뱀의 방향 전환 횟수
# snake_change_count = int(sys.stdin.readline().rstrip())
# # 뱀의 방향 전환 데이터 저장소
# data = []
# for _ in range(snake_change_count):
#     t, d = map(str, sys.stdin.readline().rstrip().split())
#     data.append((int(t), d))
#
# # 우_0 하_1 좌_2 상_3 (시계방향)
# dx = [0, -1, 0, 1]
# dy = [1, 0, -1, 0]
#
# # 뱀은 오른쪽 방향부터 간다.
# current_dir_num = 0
# current_x = 0
# current_y = 0
#
#
# def get_direction(dir_num: int, dir_char: str):
#     # 시계방향과 같이 회전을 할 때 인덱스를 사용하면 편하게됨
#     # 좌로 90도
#     if dir_char == 'L':
#         return (dir_num - 1) % 4
#     # 우로 90도
#     elif dir_char == 'D':
#         return (dir_num + 1) % 4
#
#
# for time, dir in data:
#     for t in range(time):
#         # 방향을 바꿔야 되는 시간에 도달시
#         if t == time - 1:
#             current_dir_num = get_direction(dir_num=current_dir_num, dir_char=dir)
#
#         # 다음 위치
#         current_y = current_y + dy[current_dir_num]
#         current_x = current_x + dx[current_dir_num]
#
#         # 사과를 먹을 경우, 꼬리는 움직이지 않는다.
#         if board[current_y][current_x] == 1:
#             board[current_y][current_x] = 2
#             continue
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

n = int(input())
k = int(input())
# 1행 1열 부터 보드는 시작된다. 0행과 0열들은 쓰이지 않는다.
data = list([0] * (n + 1) for _ in range(n + 1))

# 사과 위치시키기
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

# 방향 회전 정보
info = []

# 방향전환 최종 횟수
turn_time = int(input())

for _ in range(turn_time):
    x, c = input().split()
    info.append((int(x), c))

# 동 남 서 북 : 머리가 동쪽부터 시작
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
"""
내려갈 수록 남쪽으로 갈 수록 숫자가 커진다. 
[
    0:[]
    1:[]
    2:[]
]
"""


def turn(current_direction: int, next_direction: str):
    if next_direction == 'L':
        direction = (current_direction - 1) % 4
    else:
        direction = (current_direction + 1) % 4
    return direction


def simulate():
    # 시작위치
    head_x, head_y = 1, 1
    # 머리와 몸통은 7로 표시
    data[head_x][head_y] = 7
    # 머리 위치는 동쪽
    direction = 0

    # 걸린 시간
    time = 0

    # 몇번째 방향전환 info 를 이용할 것인지
    current_turn_time = 0

    # 머리와 꼬리
    q = [(head_x, head_y)]

    while True:
        # 꼬리들의 방향전환에 대해 걱정을 했었지만 current 방향에 direction 방향 숫자만 추가하면돼서 모두 잘 바뀌어 들어감.
        # 머리와 꼬리의 방향과 수만 바뀌면 되는 것
        nx = head_x + dx[direction]
        ny = head_y + dy[direction]

        # 머리가 벽을 만나거나 머리가 몸을 만나지 않을 경우
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 7:
            # 다음칸이 빈칸이라면 머리를 움직이기
            if data[nx][ny] == 0:
                data[nx][ny] = 7
                # 머리를 움직이고 q에 넣기
                q.append((nx, ny))
                # 꼬리를 pop 시키기
                px, py = q.pop(0)
                # 꼬리가 움직인 board 를 빈칸으로 변경
                data[px][py] = 0

            # 사과를 만날 경우
            if data[nx][ny] == 1:
                data[nx][ny] = 7
                q.append((nx, ny))

        # 벽이나 몸통에 부딪힐 경우
        else:
            time += 1
            break

        # Head 의 위치 변경
        head_x, head_y = nx, ny
        time += 1

        # 방향전환을 해야 할 경우
        # ex) inf = [(3,'L'),(15,'L'),(9,'D')]
        if current_turn_time < turn_time and time == info[current_turn_time][0]:
            direction = turn(current_direction=direction, next_direction=info[current_turn_time][1])
            current_turn_time += 1

        print(info[current_turn_time])
        for _ in data:
            print(_)
        print()
    return time


print(simulate())
