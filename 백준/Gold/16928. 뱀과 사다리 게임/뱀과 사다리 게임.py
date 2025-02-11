import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())

# 사다리와 뱀 정보를 딕셔너리로 저장
board = {i: i for i in range(1, 101)}  # 초기에는 자기 자신을 가리키도록 설정
for _ in range(N + M):
    x, y = map(int, input().strip().split())
    board[x] = y  # 사다리 또는 뱀 적용

# BFS 초기 설정
visited = [-1] * 101
Q = deque([1])
visited[1] = 0  # 시작 위치 1번 칸

# BFS 탐색 시작
while Q:
    x = Q.popleft()
    for dice in range(1, 7):  # 주사위는 1~6
        nx = x + dice
        if nx > 100 or visited[board[nx]] != -1:
            continue
        visited[board[nx]] = visited[x] + 1
        Q.append(board[nx])

# 정답 출력
print(visited[100])