import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
data = deque()
data.appendleft(0)
data.extend(list(map(int, sys.stdin.readline().split())))
res = []
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i <= j:
            continue
        elif data[i] == data[j]:
            continue
        else:
            res.append((i, j))

print(len(res))
