# import sys
# from collections import deque
#
# n = int(sys.stdin.readline().strip())
# graph = [[] for _ in range(n + 1)]
#
# for i in range(1, n + 1):
#     index_q_building_data = deque(sys.stdin.readline().strip().split())
#     # remove -1
#     index_q_building_data.pop()
#     r = index_q_building_data.ex
#     graph[i].append((index_q_building_data.popleft(), index_q_building_data.pop()))
# for a, b in data:
#     graph[a].append(b)
#     # 진입차수 1 증가 (b로 유입되는 간선)
#     indegree[b] += 1
#
#
#
#

import sys
from collections import deque

input = sys.stdin.readline
N = int(input())

# 각 건물 다음 지어질 건물들 리스트
building_plans = [[] for _ in range(N + 1)]
# 각 노드의 진입차수 저장
indegree = [0] * (N + 1)
# 건물 짓는데 걸리는 시간
building_time = [0] * (N + 1)

for current_building in range(1, N + 1):
    # -1 을 제외한 모든 값들
    data = list(map(int, input().split()))[:-1]
    # 현재 건물이 지어지는데에 걸리는 시간( 조건1 : 비용)
    building_time[current_building] = data[0]
    # 현재 건물이 지어지기 위해 있어야 하는 빌딩들 (조건2 : 앞서 지어져야하는 빌딩_선수건물)
    pre_buildings = data[1:]

    # 간선 연결 및 진입차수 설정
    for building in pre_buildings:
        # [선수건물의 다음 지을 current_building 데이터 저장]
        # 1 이라는 건물이 지어지기 위해서 234 가 필요한데
        # 다른 말로 2 3 4 가 지어진 후 1을 지을수 있다.
        building_plans[building].append(current_building)
        # 선수 빌딩의 수만큼 현재 건물의 진입차수가 늘어남.
        indegree[current_building] += 1


# 위상 정렬 함수
def topology_sort():
    # 각각의 빌딩을 짓기까지 걸리는 시간 (선수빌딩시간 + 현재 빌딩시간)
    res_building_times = [0] * (N + 1)
    q = deque()

    # 시작 노드 찾기(건축할 첫빌딩찾기)
    for current in range(1, N + 1):
        # 진입 차수가 0이면 시작점이나 다른 그룹
        if indegree[current] == 0:
            q.append(current)

    # q 에는 다음 건축할 빌딩의 인덱스들이 들어갈 것.
    while q:
        now = q.popleft()
        # 큐에서 꺼낸 노드 번호에 해당하는 건물을 짓는데 걸리는 시간 저장
        # 선수 건물 짓는데 걸리는 시간이 포함되어 있음!
        # 즉, '선수 건물 짓는데 걸리는 시간 + 현재 건물 짓는데 걸리는 시간'이 저장됨
        res_building_times[now] += building_time[now]
        # 빌딩 다음으로 지을 빌딩을 찾아 q에 넣기
        for next_building in building_plans[now]:
            indegree[next_building] -= 1
            # 다음 건물을 짓기 전에 선수 건물 짓는데 걸리는 시간으로 갱신 (이부분 아직 이해가 덜됨 : now 빌딩의 시간과 (누적)선수빌딩 시간을 비교할 필요가 있을가 어차피 누적이 더 많을텐데)
            res_building_times[next_building] = max(res_building_times[next_building], res_building_times[now])
            # next_building 앞서 더 지을 건물이 없으면 next_building 짓기
            if indegree[next_building] == 0:
                q.append(next_building)

    return res_building_times


answer = topology_sort()
for current_building in range(1, N + 1):
    print(answer[current_building])