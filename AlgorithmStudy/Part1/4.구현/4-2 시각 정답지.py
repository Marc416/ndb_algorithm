h = int(input())


def contains_3(time) -> int:
    if time.__contains__("3"):
        return 1
    else:
        return 0


cnt = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            time = str(i) + str(j) + str(k)
            cnt += contains_3(time)

print(cnt)
