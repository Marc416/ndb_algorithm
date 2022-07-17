import sys

number = sys.stdin.readline().rstrip()
res = 0
for idx, value in enumerate(number):
    if idx == 0:
        res = int(value)
    else:
        res = max(int(value) + res, int(value) * res)

print(res)

# # 교재 답안
# data = input()
# result = int(data[0])
# for i in range(1, len(data)):
#     num = int(data[i])
#     # 숫자가 1이나 0이면 곱하기보다 더하는 것이 값이 큼으로 더하고
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         # 그 외는 모두 곱한다.
#         result *= num
# print(result)
