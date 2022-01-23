n, m = 4, 6
rice_cake = [19, 15, 10, 17]

rice_cake.sort()

largest = 0


def binary_search(rice_cake_list, target, start, end):
    global largest
    # 비교할 end point 가 없는 경우 탈출
    if start >= end:
        return

    mid_length = (start + end) // 2
    temp_res_length = 0
    for i in rice_cake_list:
        if (part_length := i - mid_length) <= 0:
            part_length = 0
        temp_res_length += part_length

    # If res is lower than target, Move start point
    if temp_res_length < target:
        return binary_search(rice_cake_list=rice_cake_list, target=target, start=start, end=mid_length - 1)
    else:
        largest = mid_length
        # 잘리는 떡의 총길이 합이 target 보다만 크면 최대로 자를 수 있는 크기를 얻을 수 있다.
        return binary_search(rice_cake_list=rice_cake_list, target=target, start=mid_length + 1, end=end)


binary_search(rice_cake_list=rice_cake, target=m, start=0, end=rice_cake[-1])
print(largest)
