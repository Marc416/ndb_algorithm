def solution(food_times, k):
    if k >= sum(food_times):
        return -1

    # low, high = 1, 8  # 문제에서 주어진 원소의 최소, 최댓값
    low, high = 0, 1000000000  # 문제에서 주어진 원소의 최소, 최댓값
    laps, total_times, food_count = 0, 0, len(food_times)  # 바퀴 수, 총 시간, 음식 수

    # while 문의 목표 : 이분탐색으로 k초 보다 적은 초를 구한다.
    while low <= high:
        # 음식 유무와 상관없이 모든 음식을 다 먹는다고 가정하고
        # k초에 도달 할 때까지 몇바퀴를 도는지 이분탐색으로 찾기
        mid_laps = (low + high) // 2

        # laps 만큼 모든 음식을 다 먹을 때에 걸리는 시간
        # k 초 이하로 먹을때까지 찾는다.
        times = food_count * mid_laps

        # 건너뛰어야 하는 음식의 초수를 times 에 더해줘서 간극을 맞춘다.
        for f_time in food_times:
            cnt = f_time - mid_laps
            if cnt < 0:
                times += cnt

        if times <= k:  # 총 시간이 k보다 작거나 같다면, 우리가 원하는 바퀴 수일 수 있으니 각각 저장해준다.
            laps, total_times = mid_laps, times
            low = mid_laps + 1  # k보다 작으면서 최대인 값이 아닐 수 있으므로 다시 이분 탐색
        else:
            high = mid_laps - 1

    # 최대 laps 만큼 초가 제거된 food_times 로 갱신한다.
    # 음수인 초가 있겠지만 while 문에서 이미 최적해를 걸러왔으므로 양수의 음식들만 다시 탐색하면 된다.
    food_times = [time - laps for time in food_times]

    for i in range(food_count):
        # 음수인 경우 제외
        if food_times[i] <= 0:
            continue

        if food_times[i] > 0 and total_times == k:  # 음식이 남아 있고, 총 시간이 k를 만족할 경우
            return i + 1  # 현재 인덱스+1을 출력(0부터 시작하기 떄문)
        else:
            # 음식이 남아 있는 경우만 총 시간에 +1
            total_times += 1
    return -1


print(solution([4, 2, 3, 6, 7, 1, 5, 8], 16))
