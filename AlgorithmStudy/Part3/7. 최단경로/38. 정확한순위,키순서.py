import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dynamic = list([float('INF')] * (n + 1) for _ in range(n + 1))

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dynamic[a][b] = 1

for i in range(n + 1):
    dynamic[i][i] = 0

# 플로이드 워셜로 풀라고하는데 왜 그래야 되는지 모르겠다
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            dynamic[a][b] = min(dynamic[a][b], dynamic[a][k] + dynamic[k][b])

res = 0
for i in range(1, n + 1):
    count = 0
    for j in range(1, n + 1):
        # 연결되거나 연결이 되어진다면 숫자로 바퀼테니까
        if dynamic[i][j] != float('INF') or dynamic[j][i] != float('INF'):
            count += 1
    # 모드 연결된경우 -> 노드의 수만큼 연결되면 순서를 찾을 수 있음.
    if count == n:
        res += 1

print(res)
