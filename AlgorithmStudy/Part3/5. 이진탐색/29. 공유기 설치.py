import sys

n, c = map(int, sys.stdin.readline().rstrip().split())

data = list(int(sys.stdin.readline()) for _ in range(n))
data.sort()

# 공유기를 설치할 수 있는 거리의 범위 (start~end)
start = data[0]
end = data[-1]

# 공유기 거리
dist = 0

while True:
    if start > end:
        break

    # 공유기를 설치할 거리(두지점의 중간 지점 거리를 나타내기 위함)
    mid = (start + end) // 2

    # 최근 공유기가 설치된 위치
    value = data[0]

    # 공유기 수
    c_count = 1

    for i in range(1, n):
        # 공유기 설치 (설치하기로 한 거리이상인 지점일 경우 설치)
        if data[i] >= value + mid:
            value = data[i]
            c_count += 1

    # 공유기 수가 최소설치하기로한 c개이상 설치 할 수 있는 경우 (최대로 설치해야 하기 때문에)
    if c_count >= c:
        start = mid + 1
        dist = mid
    # 공유기수가 모자르면 설치할 수 있는 거리의 범위(최대거리)를 줄이기
    else:
        end = mid - 1
print(dist)
