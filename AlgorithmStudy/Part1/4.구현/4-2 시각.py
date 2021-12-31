import math


def contains_3(time) -> int:
    if time.__cotains__("3"):
        return 1


def choose_3(choice_count):
    # 10분 :6Cn
    v1 = math.factorial(6) / math.factorial(choice_count * (6 - choice_count))
    # 1분 :10Cn
    v2 = math.factorial(10) / math.factorial(choice_count * (10 - choice_count))
    # 10초 :6Cn
    v3 = math.factorial(6) / math.factorial(choice_count * (6 - choice_count))
    # 1초 :10Cn
    v4 = math.factorial(10) / math.factorial(choice_count * (10 - choice_count))

    return v1 * v2 * v3 * v4


print(choose_3(0))

# res = 0
# for i in range(0, h):
#     res += 6 * choose_3(i)
#
# print(res)
