import sys

n, x = map(int, sys.stdin.readline().rstrip().split())
li = list(map(int, sys.stdin.readline().rstrip().split()))


# x가 처음 나온 index 찾기
def find_first_x(data: list, target: int, start: int, end: int):
    if start > end:
        return None

    mid = (start + end) // 2

    # 가장 왼쪽의 target index 를 반환
    if (mid == 0 or data[mid - 1] < target) and data[mid] == target:
        # (target 의 index 가 0부터 시작하는 경우 -> 가장 왼쪽 index 라 볼 수 있음)
        return mid
    # mid 가 가리키는 숫자가 target 보다 크거나 같으면 왼쪽 section 확인
    elif data[mid] >= target:
        return find_first_x(data, target, start, mid - 1)
    # mid 가 가리키는 숫자가 target 보다 작으면 오른쪽 section 확인
    else:
        return find_first_x(data, target, mid + 1, end)


def find_last_x(data: list, target: int, start: int, end: int):
    if start > end:
        return None

    mid = (start + end) // 2

    # 가장 오른쪽의 target index 를 반환
    if (mid == n - 1 or data[mid + 1] > target) and data[mid] == target:
        return mid
    # mid 가 가리키는 숫자가 target 보다 작거나 같으면 오른쪽 section 확인
    elif data[mid] <= target:
        return find_last_x(data, target, mid + 1, end)
    # mid 가 가리키는 숫자가 target 보다 크면 왼쪽 section 확인
    else:
        return find_last_x(data, target, start, mid - 1)


def count_by_value(data: list, target: int) -> int:
    # 1. x가 처음 나온 인덱스 찾기
    first_x_idx = find_first_x(data=data, target=target, start=0, end=n - 1)

    # 2. x가 마지막으로 나온 인덱스 찾기
    last_x_idx = find_last_x(data=data, target=target, start=0, end=n - 1)

    if first_x_idx is None and last_x_idx is None:
        return -1

    return last_x_idx - first_x_idx + 1


count = count_by_value(data=li, target=x)
print(count)
print(count)
