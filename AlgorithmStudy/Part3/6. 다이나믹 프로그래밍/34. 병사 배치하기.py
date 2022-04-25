import sys

n = int(sys.stdin.readline().rstrip())
array = list(map(int, sys.stdin.readline().rstrip().split()))
# 전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치를 하고자 합니다. -> 라는 말이내림 차순 으로 배치했다는건가
array.reverse()

dp = [1] * n

for last in range(1, n):
    for prev in range(0, last):
        # 앞에있는 수보다 뒤에 있는 수가 더 크다면
        if array[prev] < array[last]:
            # last 수를 마지막 수로 가정하고 앞의 수들을 멤버로 받아들인다.
            dp[last] = max(dp[last], dp[prev] + 1)
