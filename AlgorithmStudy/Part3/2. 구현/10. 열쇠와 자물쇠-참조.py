import copy


def rotate(key: list):
    # 1. 배열을 역순으로 만든다.
    # 2. unpack operator(*) 로 2차배열을 각각의 1차배열로 반든다 [asterisk operator 라고도 한다]
    #   [[1,2,3],[1,2,3]] => [1,2,3] [1,2,3]
    # 3. zip([1,2,3],[1,2,3]) 으로 각각의 같은 인덱스 속성들을 튜플로 묶는다
    #   [(1, 1), (2, 2), (3, 3)]
    # 3. 튜플을 리스트로 변환한다.
    return list(zip(*key[::-1]))


def normal_rotate(key: list):
    key_row = len(key)
    key_col = len(key[0])
    temp_list = list([0] * key_row for _ in range(key_col))
    for i in range(key_col):
        for j in range(key_row):
            # i줄 첫번째 인덱스는 회전하면 j줄 마지막 인덱스로 간다
            temp_list[i][j] = key[j][key_col - 1 - i]
    return temp_list


def check(lock: list, lock_size: int, off_set_row: int, off_set_col: int):
    # 자물쇠에 키가 들어가서 모두 1이 나오는지 체크
    # 25, 29, 31 테스트 케이스가 풀리지 않은 이유 :
    # 자물쇠 부분만 확인해야 하는데 키부분만 확인함.
    for i in range(lock_size):
        for j in range(lock_size):
            if lock[off_set_row + i][off_set_col + j] != 1:
                return False
    return True


def merge_lock_key(temp_lock: list, rotated_key: list, key_row_size: int, key_col_size: int, x: int, y: int):
    # 키를 임시 lock 에 더하기
    for i in range(key_row_size):
        for j in range(key_col_size):
            try:
                temp_lock[x + i][y + j] += rotated_key[i][j]
            except IndexError:
                return temp_lock
    return temp_lock


def solution(key, lock):
    # 최초의 자물쇠, 키 크기를 저장
    lock_size = len(lock)
    key_row_size = len(key)
    key_col_size = len(key[0])

    off_set_row = key_row_size - 1
    off_set_col = key_col_size - 1
    # 확장한 자물쇠를 모두 돌면서 키가 자물쇠에 맞는지 체크
    for x in range(lock_size + off_set_row):
        for y in range(lock_size + off_set_col):
            # 탐색할 자물쇠 크기 =  20 * 3 - offset * 2 = 58
            array = [[0 for _ in range(58)] for _ in range(58)]

            # 가상 자물쇠에 원래의 자물쇠 넣기
            for i in range(lock_size):
                for j in range(lock_size):
                    array[off_set_row + i][off_set_col + j] = lock[i][j]

            rotated_key = copy.deepcopy(key)
            for _ in range(4):
                # 90도 회전한 키
                # rotated_key = rotate(rotated_key)
                rotated_key = normal_rotate(rotated_key)
                # 임시 lock에 회전한 키 넣기
                temp_lock = copy.deepcopy(array)
                temp_lock = merge_lock_key(temp_lock, rotated_key, key_row_size, key_col_size, x, y)

                if res := check(temp_lock, lock_size, off_set_row, off_set_col):
                    return res
    return False


print(solution(
    [[1, 0, ],
     [1, 1, ],
     [1, 1, ]],
    [[1, 1, 1],
     [1, 0, 1],
     [1, 0, 0]]))
