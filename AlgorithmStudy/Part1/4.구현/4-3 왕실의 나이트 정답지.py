input_data = input()
# Get Row
row = int(input_data[1])
# Get Column : Use Unicode (string->unicode)
column = int(ord(input_data[0])) - int(ord('a')) + 1  # 1을 더해주는 이유는 체스판이 1부터 시작하기 때문

# 8가지 경우의 수 : 하하좌, 좌좌하, 좌좌상, 상상좌, 상상우, 우우상, 우우하, 하하우
steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]

    if next_row >= 1 and next_row <= 8 \
            and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
