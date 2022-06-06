def solution(food_times, k):
    for idx, value in enumerate(food_times):
        food_times[idx] = [idx, value]

    time = 0

    while True:
        for value in food_times[:]:

            if time == k:
                if value[1] <= 0:
                    return -1
                answer = value[0] + 1
                return answer

            value[1] -= 1
            if value[1] == 0:
                food_times.remove(value)
            time += 1


print(solution([3, 1, 2], 5))
