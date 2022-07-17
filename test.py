a = [24, 3, 4, 2, 5]


def lam(x):
    return x > 10


a.sort(key=lam())

print(a)