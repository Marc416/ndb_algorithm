def solution(words, queries):
    answer = [0] * len(queries)
    # 알파벳 순으로 정렬, 길이를 오차순으로 정렬
    words.sort(key=len)
    for index, query in enumerate(queries):
        count = 0
        for word in words:
            # 전체가 ??? 인경우
            if query.count('?') == len(query):
                answer[index] = len(words)
                break

            if len(query) != len(word):
                continue

            if query[0] == '?':
                # ex ) '???bc' -> (a[3:] == 'bc')
                start = query.count('?')
                # 단어가 있는 지점 부터 끝까지
                if query[start:] == word[start:]:
                    count += 1
                answer[index] = count
                continue
            if query[-1] == '?':
                end = len(query) - query.count('?')
                # 단어가 있는 지점 부터 끝까지
                if query[:end] == word[:end]:
                    count += 1
                answer[index] = count
    return answer


s = solution(words=["frodo", "front", "frost", "frozen", "frame", "kakao"],
             queries=["fro??", "????o", "fr???", "fro???", "pro?"])
print(s)
