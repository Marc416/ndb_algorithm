import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
dynamic = list([] for _ in range(n + 1))

find_dynamic = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    dynamic[a].append(b)

# 플로이드 워셜로 풀라고하는데 왜 그래야 되는지 모르겠다
for a in range(1, n + 1):
    for b in dynamic[a]:
        find_dynamic[b] += 1
        find_dynamic[a] -= 1
print(find_dynamic)
