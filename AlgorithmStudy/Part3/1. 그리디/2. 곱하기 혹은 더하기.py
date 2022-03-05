import sys

number = sys.stdin.readline().rstrip()
res = 0
for idx, value in enumerate(number):
    if idx == 0:
        res = int(value)
    else:
        res = max(int(value) + res, int(value) * res)

print(res)
