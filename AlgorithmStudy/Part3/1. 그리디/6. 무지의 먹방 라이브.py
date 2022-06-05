def solution(food_times, k):
    food_length = len(food_times)
    time = 0
    idx = 0
    while True:
        if food_times[idx] == 0:
            idx += 1
            idx = idx % food_length
            continue

        if time == k:
            if sum(food_times) <= 0:
                return -1
            answer = idx + 1
            return answer

        food_times[idx] -= 1
        time += 1
        idx += 1
        idx = idx % food_length


print(solution([3, 1, 2], 5))
