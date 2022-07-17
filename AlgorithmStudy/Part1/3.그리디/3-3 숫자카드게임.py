# Row : n, Column : m
n, m = map(int, input().split())

big_in_min = -1


def python_min_method(data: list):
    global big_in_min
    # Find smallest item in data list
    res = min(data)
    if big_in_min < res:
        big_in_min = res


def sum_array(array: list[int]) -> int:
    size: int = len(array)
    sum: int = 0
    for iterator in range(size):
        sum += array[iterator]
    return sum


'''
public int sumArray(int[] array) {
    int size = array.length;
    int sum = 0;

    for (int iterator = 0; iterator < size; iterator++) {
        sum += array[iterator];
    }

    return sum;
}'''


def compare(data: list):
    min_val = 100000
    global big_in_min
    for i in data:
        if i < min_val:
            min_val = i
    if big_in_min < 0:
        big_in_min = min_val
    elif big_in_min < min_val:
        big_in_min = min_val


for i in range(n):
    # Get m Column Value
    input_data = list(map(int, input().split()))

    """[Solution Below]"""
    # python_min_method(input_data)
    compare(input_data)

print(big_in_min)
