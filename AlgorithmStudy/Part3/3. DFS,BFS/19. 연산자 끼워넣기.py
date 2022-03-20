import math
import sys
from itertools import permutations
import operator

n = int(sys.stdin.readline().rstrip())
input_num = list(map(int, sys.stdin.readline().rstrip().split()))

# +, -, *, /
op = list(map(int, sys.stdin.readline().rstrip().split()))
operators = []
operator_idx = ['+', '-', '*', '/']
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    # itruediv : operator 기능 중 나누기 기능 (/),
    # https://docs.python.org/ko/3.7/library/operator.html
    '/': operator.itruediv,
}

# 결과 값 세팅
max_res = -float('inf') # - inf 안쓰고 처음에 0을 대입 했다가 틀렸었음.
min_res = float('inf')

for idx, count in enumerate(op):
    if count != 0:
        for _ in range(count):
            operators.append(operator_idx[idx])

operator_permutation_set = set(permutations(operators, n - 1))
for operator_set in operator_permutation_set:
    res_temp = input_num[0]
    for idx, operator in enumerate(operator_set):
        # math.trunc 소수점 버림
        res_temp = math.trunc(ops[operator](res_temp, input_num[idx + 1]))
    max_res = max(max_res, res_temp)
    min_res = min(min_res, res_temp)

# for operator_c
print(max_res)
print(min_res)
