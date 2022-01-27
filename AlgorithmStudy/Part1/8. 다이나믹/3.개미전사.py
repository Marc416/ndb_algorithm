n = 4
k = [1, 3, 1, 5]

di = [0] * n

"""
[1] 1개 있을 경우, 인덱스 0을 선택 => [1]
[1,3] 2개 있을 경우, 인덱스 0이나 1을 선택 => [1,0] or [0,3]
[1,3,1] 3개 있을 경우, 바로전 인덱스의 최대 값을 선택 하거나 바로 전전 인덱스의 최대값(합) + 현재 array값 => di[i-1] or di[i-2] + k[i]  
[1,3,1,5] 4개 있을 경우, 바로전 인덱스의 최대 값을 선택 하거나 바로 전전 인덱스의 최대값(합) + 현재 array값 => di[i-1] or di[i-2] + k[i]  
"""

di[0] = k[0]    # 1개 있을 경우, 최대 값은 인덱스 0을선택하는 것 (점화식의 시작점을 만들어줘야함)
di[1] = max(di[0], k[1])    # 2개 있을 경우, 최대 값은 인덱스 1이나 2를 선택하는 것 (점화식의 시작점을 만들어줘야함)
for i in range(2, n):
    di[i] = max(di[i - 1], di[i - 2] + k[i])
print(di)
