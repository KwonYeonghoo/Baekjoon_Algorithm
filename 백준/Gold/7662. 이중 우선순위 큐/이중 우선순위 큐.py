import sys
import heapq
input = sys.stdin.readline

### 우선순위큐를 두 개 만들어서 풀기
### heappush(), heappop() 연산은 O(log N)
### 위 방식의 문제점: 연산이 진행됨에 따라 Max_Q와 Min_Q 간의 불일치 문제가 발생
### 해결방법: 삭제 여부를 추적할 수 있는 방법이 필요
##### 입력으로 주어지는 값을 key로 하는 딕셔너리를 생성
##### 중복된 입력이 주어질 수 있으므로, value가 0일 때 삭제된 것으로 간주, 입력된 값을 +1 하면서 관리


T = int(input().strip())
for _ in range(T):
    k = int(input().strip())  # k <= 1000000
    Q_len = 0
    isDeleted = dict()
    max_Q = []  # 값이 클수록 우선순위가 높은 큐
    min_Q = []  # 값이 작을수록 우선순위가 높은 큐
    for _ in range(k):  # O(N)
        cmd, n = input().strip().split()
        n = int(n)
        if not n in isDeleted:
            isDeleted[n] = 0
        if cmd == "I":
            heapq.heappush(max_Q, -n)  # O(logN)
            heapq.heappush(min_Q, n)
            isDeleted[n] += 1
            Q_len += 1
        else:
            if Q_len == 0:
                continue
            if n == 1:
                while max_Q:
                    val = -heapq.heappop(max_Q)  # O(logN)
                    if isDeleted[val] > 0:
                        isDeleted[val] -= 1
                        Q_len -= 1
                        break
            elif n == -1:
                while min_Q:
                    val = heapq.heappop(min_Q)
                    if isDeleted[val] > 0:
                        isDeleted[val] -= 1
                        Q_len -= 1
                        break

    max_value, min_value = None, None

    while max_Q:
        max_value = -heapq.heappop(max_Q)
        if isDeleted[max_value] > 0:
            break
        max_value = None
    while min_Q:
        min_value = heapq.heappop(min_Q)
        if isDeleted[min_value] > 0:
            break
        min_value = None

    if max_value is None or min_value is None:
        print("EMPTY")
    else:
        print(max_value, min_value)
