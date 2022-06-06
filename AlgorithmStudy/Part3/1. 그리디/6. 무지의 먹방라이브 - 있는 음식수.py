def solution(food_times, k):
    for idx, value in enumerate(food_times):
        food_times[idx] = [idx, value]

    time = 0

    while True:
        if sum(map(lambda x: x[1], food_times)) > k:
            idx, value = min(food_times, key=lambda x: x[1])
            food_count = len(food_times)
            time += food_count
            food_times.remove([idx, value])
        else:
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
