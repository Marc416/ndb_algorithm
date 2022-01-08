from collections import deque

# n, m = map(int, input().split())
n, m = 5, 6
"""
list(list(map(int, input().split())) for _ in range(n))<- 0이문에
5 6
111111
000001
111111
111111
111111
[[111111], [1], [111111], [111111], [111111]]
이렇게나옴
"""

# game_map = []
# for i in range(n):
#     game_map.append(list(map(int, input())))
game_map = [
    [1, 0, 1, 0, 1, 0],
    [1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1]]

go_four_direction = [
    (1, 0),  # 상
    (-1, 0),  # 하
    (0, -1),  # 좌
    (0, 1)]  # 우


def bfs(input_x, input_y):
    q = deque()
    q.append((input_x, input_y))
    # Check Initial Point

    while q:
        x, y = q.popleft()

        # Find 4 route
        for add_x, add_y in go_four_direction:
            next_x, next_y = x + add_x, y + add_y

            # Ignore Outside
            if next_x < 0 or next_x >= n or next_y < 0 or next_y >= m:
                continue

            # Ignore Wall
            if game_map[next_x][next_y] == 0:
                continue

            # 막다른 골목이나 더짧은 경로를 찾을 수 있도록 하는 로직이 생각이 안남.
            # => 맵에다가 count 수를 기록하면됨

            # 중요한 곳은 이부분
            if game_map[next_x][next_y] == 1:
                game_map[next_x][next_y] = game_map[x][y] + 1
                q.append((next_x, next_y))
                for i in game_map:
                    print(i)
                print()

            # Return Result
            if next_x == n - 1 and next_y == m - 1:
                return game_map[n - 1][m - 1]
    return game_map[n - 1][m - 1]


print(bfs(0, 0))
