n, m, k = map(int, input().split())
input_data = list(map(int, input().split()))
input_data.sort(reverse=True)
res = 0
# 가장 큰수가 2개 이상인 경우 m만큼 모두 곱한다.
if input_data[0] == input_data[1]:
    res = input_data[0] * m
else:
    # 가장 큰수와 두번째 큰수의 조합은 k+1이다.
    cnt = m / (k + 1)
    res_cnt = m % (k + 1)
res = cnt * k * input_data[0] + cnt * input_data[1] + res_cnt * input_data[1]
print(res)
