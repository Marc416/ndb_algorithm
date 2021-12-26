"""
[문제 요지]
1. 게임 메뉴얼에 따라 캐릭터가 이동한 칸 수를 출력
2. 언제 이동이 끝나는가?
->  ...멈춘다. 라는 구절에서
=> "조건을 반복해서 언젠가 맞을 조건에 반복문을 종료시킨다"
3. 이동메뉴얼의 조건은 어떻게 나누는가?
-> ..1단계로 돌아간다. => 총 2가지 조건이 있을 것이다.
4. 이동할 x,y축의 기준은?
-> 1사분면을 x축 기준으로 뒤집은것과 같음
=> 우리가 원래 알던 ,xy가 아님

[캐릭터 이동의 룰]
1.
if 현재위치에서 왼쪽 방향의 블럭이 육지이고 가보지 않은 칸이라면 :
  왼쪽칸으로 방향을 돌리고 전진
else:
  왼쪽칸으로 방향만 돌리기

finally:
    1단계 다시 반복

2.
if 네방향을 모두 탐색을 했는 이미 가본 칸이거나, 바다라면:
    뒤로가기(방향은 유지)
    if 만약 뒤가 바다라서 갈 수가 없다면:
        게임종료

[준비사항]
1. 이미 간 곳인지 알 수 있는 데이터가 있어야 함
-> Set 을 써도 되고, 게임 맵을 그대로 가져와서 1로 표시해도 되고, 방법은 다양
"""

# [Input]
n, m = 4, 4
# n, m = map(int, input().split())

'''
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
'''
went = [[0] * m for _ in range(n)]

# [Input]
# 현재좌표와 방향 받기 (x: 상하;낮을 수록 top, y :좌우)
# (중요)일반적 우리가 알고있는 x,y축이 아님. 축의 중심의 위치와 진행방향이 다름.
x, y, direction = 1, 1, 0
# x, y, direction = map(int, input().split())

# 현재있는 곳을 1로 체크하기
went[x][y] = 1

# [Input]
# 게임맵을 받아오기 한줄식 입력받으므로 한줄씩 세팅
game_map = [[1, 1, 1, 1], [1, 0, 0, 1], [1, 1, 0, 1], [1, 1, 1, 1]]
# game_map = []
# for i in range(n):
#     game_map.append(list(map(int, input().split())))

# 북동남서 방향정의
# : x,y에 몇을 더해야 하는지
dx = [-1, 0, 1, 0]
# (여기서 y는 좌우)
dy = [0, 1, 0, -1]


def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


# 시작하는 값이 이미 방문을 할 수 있는 위치이므로 카운트 1로 시작
# [최종 답안이 될 변수]
count = 1

# 4방면이 바다이거나 가본 곳이라면(4군데 모두 탐색했을 경우) 게임종료
# [종료 Trigger]
turn_time = 0

while True:
    # 현재방향에서의 왼쪽 블럭의 위치 정보 가져오기 ; n-> next
    turn_left()
    turn_time += 1
    # 실제 데이터를 변경하지 않고 미래의 데이터변수를 만들어서 작동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 왼쪽 블럭이 게임맵에서 육지이고, 내가 가본 곳이 아니면 전진
    if game_map[nx][ny] == 0 and went[nx][ny] == 0:
        went[nx][ny] = 1
        x = nx
        y = ny
        # 방문 카운트 더하기
        count += 1
        # while 문을 다시 돌 것이기 때문에 turn_time Reset
        turn_time = 0
        continue

    # 4방면의 왼쪽 블럭이 게임맵에서 바다 이거나, 가본 곳이라면
    if turn_time == 4:
        # 뒤로 후진
        nx = x - dx[direction]
        ny = y - dy[direction]

        # 만약 뒤가 바다이면 멈춤
        if game_map[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
