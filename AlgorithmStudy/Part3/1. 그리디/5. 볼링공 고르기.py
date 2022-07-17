import sys
# from collections import deque
#
# n, m = map(int, sys.stdin.readline().split())
# # 볼링공은 1번부터 사용할 것이기 때문에 0번 인덱스에 임의 값을 채운다.
# # 가독성을 위해 deque을 이용.
# data = deque()
# data.appendleft(0)
# # 두번째 줄의 입력값을 list로 만들어 병합한다.
# data.extend(list(map(int, sys.stdin.readline().split())))
#
# res = []
# # 공의 개수가 최대 1000개 이므로 두개를 뽑는다고 가정할 때 1,000,000미만의 연산이 이뤄짐
# # -> 2000만번보다 연산수가 적으므로 2중 반복문을 쓸 수 있다고 판단.
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         # 1. A,B는 (인덱스가)동일한 볼링공을 뽑을 수 없다. (물리적으로 불가능)
#         # 2. A,B가 고른 공의 순서를 고려하지 않는다.
#         # (A: 1번, B: 2번) == (A: 2번, B: 1번)
#         if i <= j:
#             continue
#         # 같은 무게의 공은 고를 수 없다.
#         elif data[i] == data[j]:
#             continue
#         else:
#             res.append((i, j))
#
# print(len(res))

n, m = map(int, sys.stdin.readline().split())
ball_weight = list(map(int, sys.stdin.readline().split()))
weight_list = [0] * (m + 1)
for weight in ball_weight:
    weight_list[weight] += 1
cnt = 0
for i in range(1, m + 1):
    # 같은 무게의 공은 다른 그룹에 들어가게 되므로, 생겨날 그룹의 수만큼 전체 볼링공으로부터 제외 시킨다.
    n -= weight_list[i]
    # (같은 무게의 공 수) * 나머지공 = 만들 수 있는 조합.
    cnt += weight_list[i] * n

