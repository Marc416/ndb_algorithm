import sys

# n = int(sys.stdin.readline().rstrip())
# my_part = list(map(int, sys.stdin.readline().rstrip().split()))
# m = int(sys.stdin.readline().rstrip())
# wanted_part = list(map(int, sys.stdin.readline().rstrip().split()))
n = 5
my_part = [8, 3, 7, 9, 2]
m = 3
wanted_part = [5, 7, 9]
my_part.sort()


def binary_search(my_part, target, start, end):
    # Range Check
    if start < 0 or end >= len(my_part):
        return
    # If out of range, There is no data
    if start <= end:
        mid = (start + end) // 2
    else:
        raise Exception('No data')

    if my_part[mid] == target:
        return 'yes'
    elif my_part[mid] > target:
        return binary_search(my_part=my_part, target=target, start=start, end=mid - 1)
    elif my_part[mid] < target:
        return binary_search(my_part=my_part, target=target, start=mid + 1, end=end)


for i in wanted_part:
    try:
        print(binary_search(my_part=my_part, target=i, start=0, end=len(my_part) - 1))
    except Exception as e:
        print(e)
