import sys

data = sys.stdin.readline().rstrip()
answer_len = len(data)
for step in range(1, len(data) // 2 + 1):
    # 압축된 문자열 결과
    compressed = ''
    # 비교하기위해 step 만큼의 문자 추출 (1자리, 2자리, 3자리...)
    prev = data[0:step]
    # 비교할 문자에 대한 카운트 1
    count = 1
    # 위에서 비교할 문자를 정하고
    # 비교할 문자를 제외한 문자열부터 비교
    for j in range(step, len(data), step):
        if prev == data[j:j + step]:
            count += 1
        else:
            # 비교할 문자 패턴과 다른 패턴이 나오면 결과를 저장.
            # prev와 같은 패턴이 연속 2개 이상이면 '숫자 + prev'
            compressed += str(count) + prev if count >= 2 else prev
            # 새로 비교할 문자열 정하기 (현재인덱스 + 다음인덱스)
            prev = data[j:j + step]
            # 비교할 문자에 대한 카운트 1
            count = 1

    compressed += str(count) + prev if count >= 2 else prev
    answer_len = min(answer_len, len(compressed))
print(answer_len)
# aaaabbabbabb
