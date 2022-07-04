import copy
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
class_room = []
for line in range(n):
    class_room.append(list(map(str, sys.stdin.readline().rstrip().split())))

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def teacher_queue(class_room: list) -> deque:
    queue = deque()
    for i in range(n):
        for j in range(n):
            if class_room[i][j] == 'T':
                queue.append((i, j))
    return queue


def bfs_teacher_chase_student(temp_class_room: list):
    """ 선생님이 4방으로 쫓기 """
    copy_teacher_queue = copy.deepcopy(teachers)
    for x, y in list(copy_teacher_queue):
        for i in range(4):
            temp_queue = deque()
            temp_queue.append((x + dx[i], y + dy[i]))
            while temp_queue:
                nx, ny = temp_queue.pop()
                # 경계인경우 제외
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue

                # 벽인경우 제외
                if temp_class_room[nx][ny] == 'O':
                    break

                # 학생을 한명이라도 찾은 경우
                if temp_class_room[nx][ny] == 'S':
                    return 'NO'
                if temp_class_room[nx][ny] == 'X':
                    temp_queue.append((nx + dx[i], ny + dy[i]))

    return 'YES'


def make_wall(wall_cnt: int):
    global res
    if wall_cnt == 3:
        temp_class_room = copy.deepcopy(class_room)
        if bfs_teacher_chase_student(temp_class_room) == 'YES':
            res = 'YES'
        return

    for i in range(n):
        for j in range(n):
            if class_room[i][j] == 'X':
                class_room[i][j] = 'O'
                make_wall(wall_cnt + 1)
                if res == 'YES':
                    break
                # 경우의 수 교체
                class_room[i][j] = 'X'
    return


teachers = teacher_queue(class_room)
res = 'NO'
if len(teachers) != 0:
    make_wall(0)
else:
    res = 'YES'
print(res)
