# n, m = map(int, input().split())
n, m = 4, 5
ice_bucket = []
# for i in range(n):
#     ice_bucket.append(list(map(int, input())))
ice_bucket = [
    [0, 0, 1, 1, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

four_direction = [
    (1, 0),  # 상
    (-1, 0),  # 하
    (0, -1),  # 좌
    (0, 1)]  # 우


def dfs(current_x, current_y):
    # Outside
    if current_x < 0 or current_y < 0 or current_x >= n or current_y >= m:
        return False

    # Wall
    if ice_bucket[current_x][current_y] == 1:
        return False

    # Correct
    if ice_bucket[current_x][current_y] == 0:
        ice_bucket[current_x][current_y] = 1

        for nx, ny in four_direction:
            next_x = current_x + nx
            next_y = current_y + ny

            # Return 결과를 사용하기 위한 것이 아닌 아래 FOR 문에서
            # 타겟한 지점으로 부터 연결된 모든 0들을 제거하기 위한 수단
            dfs(next_x, next_y)

        # 0이 하나라도 있기때문에 True
        return True

    return False


result = 0

# 0으로 연결된 것들을 하나의 덩어리로 카운팅하는 것이 핵심

# 세로
for i in range(n):
    # 가로
    for j in range(m):
        if dfs(i, j):
            result += 1
            for f in ice_bucket:
                print(f)
            print()

print(result)
