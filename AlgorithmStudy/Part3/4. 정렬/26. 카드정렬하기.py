import sys
import heapq

n = int(sys.stdin.readline().rstrip())
# 카드 입력
card_q = []
for _ in range(n):
    card_q.append(int(sys.stdin.readline().rstrip()))

# 카드리스트를 큐로 전환
heapq.heapify(card_q)

result = 0

while card_q is not None:
    # card_q에 2개를 pop 하고 이전 결과 1개를 푸시 함.
    # 마지막 1장의 카드가 남기전의 단계에서 카드를 계산 하였으므로
    # 1장남은 card_q가 될 때 종료.
    if len(card_q) <= 1:
        break
    # 큐중 가장 작은 수 pop
    card_1 = heapq.heappop(card_q)
    card_2 = heapq.heappop(card_q)

    temp_total = card_1 + card_2
    result += temp_total
    # heappush, append 비교하기
    heapq.heappush(card_q, temp_total)
    card_q.append(temp_total)
    print(card_q)
print(result)
