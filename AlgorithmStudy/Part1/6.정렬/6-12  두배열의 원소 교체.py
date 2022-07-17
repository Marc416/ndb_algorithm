# n, k = map(int, input().split())
# a = list(map(int, input().split()))
# b = list(int(input().split()))

a = [1, 2, 5, 4, 3]
b = [5, 5, 6, 6, 5]
k = 3
a_sort = sorted(a)  # 오름차순 정렬
b_sort = sorted(b, reverse=True)  # 내림차순 정렬
for i in range(k):
    a_sort[i], b_sort[i] = b_sort[i], a_sort[i]

print(sum(a_sort))
# print(a_sort)
# print(b_sort)
