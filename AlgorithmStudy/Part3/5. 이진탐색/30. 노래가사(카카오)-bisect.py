from bisect import bisect_left, bisect_right


def count_by_range(words: list, left, right):
    left_index = bisect_left(words, left)
    right_index = bisect_right(words, right)
    return right_index - left_index


def solution(words, queries):
    # 각 가사 단어의 길이는 1 이상 10,000 이하로 빈 문자열인 경우는 없습니다. -> 10001

    # 접미사용 : abc??
    sorted_words = list([] for _ in range(10001))
    # 접두사용 : ??abc -> cba??
    reverse_words = list([] for _ in range(10001))

    answer = [0] * len(queries)

    # 단어개수별로 리스트화 시키기
    for word in words:
        sorted_words[len(word)].append(word)
        reverse_words[len(word)].append(word[::-1])

    for i in range(10001):
        sorted_words[i].sort()
        reverse_words[i].sort()

    for index, query in enumerate(queries):
        # 접두사에 물음표
        if query[0] == '?':
            query = query[::-1]
            res = count_by_range(reverse_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
            answer[index] = res
            continue
        # 접미사에 물음표
        if query[-1] == '?':
            res = count_by_range(sorted_words[len(query)], query.replace('?', 'a'), query.replace('?', 'z'))
            answer[index] = res
            continue
    return answer


s = solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"],
             queries=["fro??", "????o", "fr???", "fro???", "pro?"])
print(s)
