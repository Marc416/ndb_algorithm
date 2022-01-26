n = 26

"""
1 -> 0
2 -> 1 # /2(1) or -1(1)
3 -> 1 # /3(1) or -1(2),-1(1)
4 -> 2 # /2(2), /2(1) or -1(3), -1(2), -1(1)
5 -> 3 # -1(4), /2(2), /2(1) or -1(4)..., -1(1)
.
.
"""
di = [0] * 3001


def search(target_num):
    for i in range(2, target_num + 1):
        di[i] = di[i - 1] + 1
        if target_num % 2 == 0:
            di[i] = min(di[i], di[i // 2] + 1)
        if target_num % 3 == 0:
            di[i] = min(di[i], di[i // 3] + 1)
        if target_num % 5 == 0:
            di[i] = min(di[i], di[i // 5] + 1)


search(n)
print(di[n])
