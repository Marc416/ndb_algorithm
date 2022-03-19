import sys

# 시험관의 크기, 바이러스의 종류
n, k = map(int, sys.stdin.readline().rstrip().split())

# 바이러스 위치 정보 graph set
graph = list([0] * (n + 1) for _ in range(n + 1))
virus_q = []

# 1. n*n의 시험관에 입력받은 바이러스들을 위치 시킨다.
for i in range(1, n + 1):
    graph[i][1:] = list(map(int, sys.stdin.readline().rstrip().split()))

    # 바이러스들을 리스트에 넣기
    for j in range(1, n + 1):
        if graph[i][j] != 0:
            # x 행, y열, virus num, 증식 count
            virus_q.append([i, j, graph[i][j]])

# s,x,y 입력받기
s, x, y = map(int, sys.stdin.readline().rstrip().split())

# 상, 하, 좌, 우 (개인적으로 상하좌우 나오는 문제를 많이 풀어봐야 할거 같음)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def move_virus(virus: list):
    x = virus[0]
    y = virus[1]
    number = virus[2]

    for i in range(4):
        # 바이러스의 다음 행선지
        nx = x + dx[i]
        ny = y + dy[i]

        # 2) 시험관의 범위가 아닌 경우 증식하지 못한다.
        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue

        # 3) 증식하려는 칸에 이미 바이러스가 있다면 증식하지 못한다.
        if graph[nx][ny] != 0:
            continue

        virus_q.append([nx, ny, number])
        graph[nx][ny] = number

    return


for _ in range(s):
    virus_q.sort(key=lambda data: data[2])
    for _ in range(len(virus_q)):
        q = virus_q.pop(0)
        move_virus(q)

    for _ in graph:
        print(_)
    print()

# 결과 출력 : s초 이후 x행,y열의 바이러스(바이러스가 없는 경우는 0으로 이미 만들었기
# 때문에 따로 조건을 주지 않아도 됨)
print(graph[x][y])
