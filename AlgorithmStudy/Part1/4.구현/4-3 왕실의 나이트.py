# 수평의 경우의 수 4개
# 수직의 경우의 수 4개

data = input()
x_standard = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

x, y = x_standard[data[0]], int(data[1])
# 상하좌우 0,1,2,3
mx = [-1, 1, 0, 0]
my = [0, 0, -1, 0]

cnt = 0


def validate_pos(pos_x, pos_y):
    if pos_x > 8 or pos_x < 1:
        return 0
    if pos_y > 8 or pos_y < 1:
        return 0
    else:
        return 1


# 상상 좌
temp_x = x + mx[0] + mx[0] + mx[2]
temp_y = y + my[0] + my[0] + my[2]
cnt += validate_pos(temp_x, temp_y)

# 상상 우
temp_x = x + mx[0] + mx[0] + mx[3]
temp_y = y + my[0] + my[0] + my[3]
cnt += validate_pos(temp_x, temp_y)
# 하하 좌
temp_x = x + mx[1] + mx[1] + mx[2]
temp_y = y + my[1] + my[1] + my[2]
cnt += validate_pos(temp_x, temp_y)
# 하하 우
temp_x = x + mx[1] + mx[1] + mx[3]
temp_y = y + my[1] + my[1] + my[3]
cnt += validate_pos(temp_x, temp_y)
# 우우 상
temp_x = x + mx[3] + mx[3] + mx[0]
temp_y = y + my[3] + my[3] + my[0]
cnt += validate_pos(temp_x, temp_y)
# 우우 하
temp_x = x + mx[3] + mx[3] + mx[1]
temp_y = y + my[3] + my[3] + my[1]
cnt += validate_pos(temp_x, temp_y)
# 좌좌 상
temp_x = x + mx[2] + mx[2] + mx[0]
temp_y = y + my[2] + my[2] + my[0]
cnt += validate_pos(temp_x, temp_y)
# 좌좌 하
temp_x = x + mx[2] + mx[2] + mx[1]
temp_y = y + my[2] + my[2] + my[1]
cnt += validate_pos(temp_x, temp_y)

print(cnt)
