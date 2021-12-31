# 부산(0), 창원(1), 서울(2)에 넣을 리스트 2차배열 초기화
graph = [[] for _ in range(3)]
# Add 부산 데이터 : 창원으로 가는 길 2개, 서울로 가는 길 3개
graph[0].append((1, 2))
graph[0].append((2, 3))
# Add 창원 데이터: 부산으로 가는 2개
graph[1].append((0, 2))
# Add 서울 데이터 : 부산으로 가는길 3개
graph[2].append((0, 3))
print(graph)


def find_changwon(city_data, count):
    # 재귀함수 끝내는 곳 : 가지고있는 city 데이터길이를 넘어가는 경우 OUT
    if count >= len(city_data):
        print("창원과 연결되지 않았습니다")
        return False
    # 튜플의 첫번째항(City:창원일 경우)
    if city_data[0] == 1:
        print("창원 연결됨")
        print(f"다리는 {city_data[1]} 개")
        return True
    else:
        return find_changwon(city_data, count + 1)


# 서울 -> 창원
for idx, city_data_tuple_list in enumerate(graph):
    if idx == 2:
        find_changwon(city_data_tuple_list, 0)
    else:
        continue
#
# # 리스트를 enumerate로 감싸면 인덱스와 밸류로 출력해서 값을 알 수 있다.
# for idx, value in enumerate(graph):
#     # 서울 도시 데이터를 찾기
#     if idx == 2:
#         # 서울과 연결된 관계 리스트들 중에서 창원과 연결된 자료 찾기
#         for j in graph[idx]:
#             if j[0] == 1:
#                 print("창원 연결됨")
#                 print(f"다리는 {j[1]} 개")
#             else:
#                 print("창원 연결안됨")
