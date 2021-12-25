n = int(input())
nav = input().split()
rule = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
pos = (1, 1)
for r in nav:
    # 입력받은 nav에 따라 네비게이션 규칙을 현재 위치에 더해 temp_pos를 만든다
    add_pos = rule[r]
    '''
    1. 미리 주어진 조건들을 튜플로 만들어 합치기만 하면 되게끔 만든다.
    '''
    temp_pos = (pos[0] + add_pos[0], pos[1] + add_pos[1])
    '''
    2. n과 0을 끝지점으로 선택해서 이 숫자를 넘지 않도록 한다.
    '''
    # y축의 위치가 1보다 작거나 n보다 크면 무시한다. -> 해당문제에서는 y축이 좌우를 결정한다
    if 1 > temp_pos[1] or temp_pos[1] > n:
        continue
    # x축의 위치가 1보다 작거나 n보다 크면 무시한다. -> 해당문제에서는 x축이 상하를 결정한다
    if n < temp_pos[0] or temp_pos[0] < 1:
        continue
    pos = temp_pos
print(pos)
