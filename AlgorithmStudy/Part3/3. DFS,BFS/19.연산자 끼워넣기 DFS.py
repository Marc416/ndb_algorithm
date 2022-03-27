import sys

N = int(sys.stdin.readline().rstrip())
num = list(map(int, sys.stdin.readline().rstrip().split()))
op = list(map(int, sys.stdin.readline().rstrip().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9

# dy = []


def dfs(depth, total, plus, minus, multiply, divide):

    global maximum, minimum
    # 마지막 연산자까지 계산을 끝냈다면
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    # temp_res = ''.join(map(str, [plus, minus, multiply, divide]))
    # if temp_res in dy:
    #     return

    """ 연산을 한 연산자에는 -1 을 더한다. """
    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
        # mid_res = ''.join(map(str, [plus - 1, minus, multiply, divide]))
        # dy.append(mid_res)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
        # mid_res = ''.join(map(str, [plus, minus - 1, multiply, divide]))
        # dy.append(mid_res)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
        # mid_res = ''.join(map(str, [plus, minus, multiply - 1, divide]))
        # dy.append(mid_res)
    if divide:
        # int 로 변형하여 소수잠 아래자리는 버린다.
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)
        # mid_res = ''.join(map(str, [plus, minus, multiply, divide - 1]))
        # dy.append(mid_res)


# 연산할 다음 숫자인덱스(깊이), (연산한)현재 숫자, +, -, *, /
dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)
