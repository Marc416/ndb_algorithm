# 2
# 3 4
# 1 3 3 2 2 1 4 1 0 6 4 7
# 4 4
# 1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2

import sys

t = int(sys.stdin.readline().rstrip())
for _ in range(t):

    n, m = map(int, sys.stdin.readline().rstrip().split())
    input_data = list(map(int, sys.stdin.readline().rstrip().split()))
    dp = []
    # 1차배열을 2차배열로 전환
    for i in range(n):
        # 각행에 들어갈 data 의 시작 점 index 추출
        start = i * m
        # start~m개 만큼 dp에 append
        dp.append(input_data[start:start + m])

    # dp의 배열을 계산하여 재배열 하기
    # 중요 : for 문 순서를 j열(1~m) 부터하는것은 각행의 i열 부터 검사하기 때문에
    # 계산에 영향을 미친다. (그림참조)
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위 value
            if i == 0:
                # 가장 위의 index 인 경우 범위 밖이므로 값을 가질 수 없다
                left_up = 0
            else:
                left_up = dp[i - 1][j - 1]
            # 왼쪽 아래 value
            if i == n - 1:
                # 가장 아래의 index 인 경우 범위 밖이므로 값을 가질 수 없다
                left_down = 0
            else:
                left_down = dp[i + 1][j - 1]
            # 왼쪽 value
            left = dp[i][j - 1]

            dp[i][j] = dp[i][j] + max(left_down, left, left_up)

    print(dp)
