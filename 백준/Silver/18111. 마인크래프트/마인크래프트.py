import sys

N, M, B = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

valid_times = {}  # {height: process_time} 형태로 저장

for height in range(257):  # 0 ~ 256 평탄화 높이
    inventory = B
    process_time = 0  # 작업하는 데 걸리는 시간

    for i in range(N):
        for j in range(M):
            diff = arr[i][j] - height  # 블록 높이 차이

            if diff > 0:  # 현재 높이가 목표보다 크면 제거 (2초)
                process_time += 2 * diff
                inventory += diff
            elif diff < 0:  # 현재 높이가 목표보다 작으면 추가 (1초)
                process_time += -diff
                inventory -= -diff

    if inventory >= 0:  # 인벤토리에 블록이 충분할 때만 저장
        valid_times[height] = process_time

# 최소 시간이 걸리는 높이 찾기 (가장 높은 높이 우선)
min_time = min(valid_times.values())
best_height = max(height for height, time in valid_times.items() if time == min_time)

print(min_time, best_height)
