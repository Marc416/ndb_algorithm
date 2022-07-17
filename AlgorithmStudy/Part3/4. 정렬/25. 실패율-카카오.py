def solution(N, stages):
    # 스테이지에 도달한 유저가 없는 경우 해당 스테이지의 실패율은 0 으로 정의한다.
    temp_answer = [0] * N
    for i in range(1, N + 1):
        in_stage_not_clear_player = 0  # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수
        clear_stage_player = 0  # 스테이지를 클리어한 플레이어

        in_stage_player = 0
        # 스테이지에 도달한 플레이어 수 =
        # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 + 스테이지를 클리어한 플레이어

        for j in stages:
            # 스테이지에 도달했으나 아직 클리어하지 못한 플레이어
            if i == j:
                in_stage_not_clear_player += 1
            # 스테이지를 클리어한 플레이어
            if i < j:
                clear_stage_player += 1
        # 스테이지에 도달한 플레이어 수
        in_stage_player = in_stage_not_clear_player + clear_stage_player

        # 스테이지별 실패율 입력
        if in_stage_player != 0:
            temp_answer[i - 1] = (i, in_stage_not_clear_player / in_stage_player)
        else:
            temp_answer[i - 1] = (i, 0)
        #     (0,1),(1,0),(3,0)
        # (0,1,3)

        # 정렬
    temp_answer.sort(key=lambda x: -x[1])
    answer = list(list(zip(*temp_answer))[0])

    return answer


print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))

"""
1. 문제 풀이를 한다.
실패율 : 
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
-> 해석 하자면
len(stage_index 인 원소) / len(stage_index 이상인 원소)

    1) stage 에 대한 실패율 리스트를 만든다. 
2. 정렬로 시간복잡도를 줄인다.

"""
