# n = int(input())
#
# input_data = [int(input()) for _ in range(n)]

input_data = [2, 4, 44]
# Sort it self
input_data.sort(reverse=True)

print(input_data)

input_data = [2, 4, 3, 22, 44]
# Copy
res = sorted(input_data, reverse=True)
print(res)
