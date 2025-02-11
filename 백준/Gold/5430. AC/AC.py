import sys
from collections import deque

T = int(input())  # 테스트 케이스 개수

for _ in range(T):
    is_reversed = False  # 뒤집기 여부
    command = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())

    # 배열 입력받기 (예외 처리 포함)
    arr_input = sys.stdin.readline().strip()
    if n == 0:
        Q = deque()
    else:
        Q = deque(map(int, arr_input[1:-1].split(",")))  # 리스트에서 괄호 제거 후 변환

    error_flag = False  # 에러 여부 확인

    for cmd in command:
        if cmd == "R":
            is_reversed = not is_reversed
        elif cmd == "D":
            if not Q:
                print("error")
                error_flag = True
                break
            if is_reversed:
                Q.pop()
            else:
                Q.popleft()

    if not error_flag:
        if is_reversed:
            Q.reverse()
        print("[" + ",".join(map(str, Q)) + "]")
