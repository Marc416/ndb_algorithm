"""
TEST CASE
5
-15 -6 1 3 7
"""

# from bisect import bisect_left
import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().rstrip().split()))


# """
# https://docs.python.org/ko/3/library/bisect.html#searching-sorted-lists
# """
#
#
# def index_and_value_equal_finder(_data: list, _target: int):
#     """
#     Locate the leftmost value exactly equal to x
#     and index equals to value
#     """
#     _index = bisect_left(_data, _target)
#
#     if _index == _target and _data[_index] == _target:
#         return _index
#
#
# for i in range(n):
#     if res := index_and_value_equal_finder(_data=data, _target=i):
#         print(res)


def binary_search(array, start, end):
    if start > end:
        return None

    mid = (start + end) // 2
    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    else:
        return binary_search(array, mid + 1, end)


index = binary_search(array=data, start=0, end=n)

if index is None:
    print(-1)
else:
    print(index)
