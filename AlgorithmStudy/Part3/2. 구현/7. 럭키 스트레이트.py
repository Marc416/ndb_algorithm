import sys

data = sys.stdin.readline().rstrip()
left_sum = 0
right_sum = 0
for i in data[:len(data) // 2]:
    left_sum += int(i)
for j in data[len(data) // 2:]:
    right_sum += int(j)
if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
