import sys
import heapq

n = int(sys.stdin.readline().rstrip())
card_q = []
for _ in range(n):
    card_q.append(int(sys.stdin.readline().rstrip()))
heapq.heapify(card_q)

result = 0
while card_q is not None:
    if len(card_q) <= 1:
        break
    # 큐중 가장 작은 수 pop
    card_1 = heapq.heappop(card_q)
    card_2 = heapq.heappop(card_q)

    temp_total = card_1 + card_2
    result += temp_total
    card_q.append(temp_total)

print(result)
