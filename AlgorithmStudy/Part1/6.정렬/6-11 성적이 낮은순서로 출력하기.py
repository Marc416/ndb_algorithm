n = int(input())

# # 생각했던것
# input_data = [map((str, int), input().split()) for _ in range(n)]

input_data = []
for _ in range(n):
    name, score = input().split()
    input_data.append((name, int(score)))

# lambda 의 콜론 앞부분은 매개변수, 뒷부분은 return 에 해당 하는 함수
# print((lambda x, y: x + y)(10, 20)) 이런식으로도 사용 가능
res = sorted(input_data, key=lambda x: x[1])
print(res)


