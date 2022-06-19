import copy


def rotate(key: list):
    # 1. 배열을 역순으로 만든다.
    # 2. zip() 과 unpack operator(*) 으로 각각의 같은 인덱스 속성들을 튜플로 묶는다
    # 3. 튜플을 리스트로 변환한다.
    return list(zip(*key[::-1]))


def check(lock: list, key_size: int, off_set: int):
    # 자물쇠에 키가 들어가서 모두 1이 나오는지 체크
    for i in range(key_size):
        for j in range(key_size):
            if lock[off_set + i][off_set + j] != 1:
                return False
    return True


def merge_lock_key(temp_lock: list, rotated_key: list, x: int, y: int):
    # 키를 임시 lock 에 더하기
    key_size = len(rotated_key)
    for i in range(key_size):
        for j in range(key_size):
            temp_lock[x + i][y + j] += rotated_key[i][j]

    return temp_lock


def solution(key, lock):
    # 최초의 자물쇠, 키 크기를 저장
    lock_size = len(lock)
    key_size = len(key)

    # key 의 앞뒤로 m-1 개만큼의 [0,0,...] 을 확장
    off_set = key_size - 1
    # 확장한 자물쇠를 모두 돌면서 키가 자물쇠에 맞는지 체크
    for x in range(lock_size + off_set):
        for y in range(lock_size + off_set):
            # 탐색할 자물쇠 크기 =  20 * 3 - offset * 2 = 58
            array = [[0 for _ in range(58)] for _ in range(58)]

            # 가상 자물쇠에 원래의 자물쇠 넣기
            for i in range(lock_size):
                for j in range(lock_size):
                    array[off_set + i][off_set + j] = lock[i][j]

            rotated_key = key
            for _ in range(4):
                # 90도 회전한 키
                rotated_key = rotate(rotated_key)
                # 임시 lock에 회전한 키 넣기
                temp_lock = copy.deepcopy(array)
                temp_lock = merge_lock_key(temp_lock, rotated_key, x, y)

                if res := check(temp_lock, key_size, off_set):
                    return res
    return False


print(solution(
    [[1, 0, 0],
     [1, 1, 0],
     [1, 1, 1]],
    [[1, 1, 1],
     [0, 0, 1],
     [1, 0, 0]]))
