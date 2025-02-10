import sys
import heapq


N = int(input())
# 0 이 아닌 정수: 추가
# 0: 절댓값이 가장 작은 값 출력, 제거/ 비어있는 경우 0 출력
# 우선순위 큐
# heapq.heappush(heap, (priority, value))
# priority 값을 잘 설정하면 될 듯

heap = []
for _ in range(N):
    n = int(sys.stdin.readline().strip())
    if n != 0:
        heapq.heappush(heap, (abs(n), n))  # (절댓값=우선순위, n)
    else:
        if len(heap) == 0:
            print(0)
            continue
        print(heapq.heappop(heap)[1])
