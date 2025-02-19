import sys
input = sys.stdin.readline

N = int(input().strip())
arr = [[c for c in input().strip()] for _ in range(N)]

# 1. 인접한 사탕의 색이 다른 것끼리 교환
# 2. 교환된 상태의 배열에서 가장 긴 연속된 사탕의 길이 구하기
# 3. 원위치 시키기


def OOB(nx, ny):
    return nx >= N or ny >= N


dx = [1, 0]
dy = [0, 1]


def get_longest_candy(arr):
    max_row = -1
    max_col = -1
    for i in range(N):
        target_row = arr[i][0]
        target_col = arr[0][i]
        row_temp = 1
        col_temp = 1
        for j in range(1, N):
            if arr[i][j] == target_row:
                row_temp += 1
            else:
                target_row = arr[i][j]
                row_temp = 1
            max_row = max(row_temp, max_row)

            if arr[j][i] == target_col:
                col_temp += 1
            else:
                target_col = arr[j][i]
                col_temp = 1
            max_col = max(col_temp, max_col)
    return max(max_col, max_row)


result = -1
for i in range(N):
    for j in range(N):
        for dir in range(2):
            nx = i + dx[dir]
            ny = j + dy[dir]
            if OOB(nx, ny) or arr[nx][ny] == arr[i][j]:
                continue
            arr[nx][ny], arr[i][j] = arr[i][j], arr[nx][ny]
            result = max(result, get_longest_candy(arr))
            arr[nx][ny], arr[i][j] = arr[i][j], arr[nx][ny]

print(result)