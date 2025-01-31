import sys

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
colored = [[-1] * N for _ in range(N)]


def get_size(x, y, n):
    """
    색종이의 크기를 구하는 함수
    Args:
        x (int): 색종이의 왼쪽 위 x 좌표
        y (int): 색종이의 왼쪽 위 y 좌표
        n (int): 색종이 한 변의 길이
    """
    size = 0
    for i in range(x, x + n):
        for j in range(y, y + n):
            size += arr[i][j]
    return size


white = 0
blue = 0

division = 1
while division <= N:
    len = int(N / division)
    for i in range(0, N, len):
        for j in range(0, N, len):
            if colored[i][j] != -1:
                continue
            size = get_size(i, j, len)
            if size == 0:
                for a in range(i, i + len):
                    for b in range(j, j + len):
                        colored[a][b] = 0
                white += 1
            elif size == len**2:
                for a in range(i, i + len):
                    for b in range(j, j + len):
                        colored[a][b] = 1
                blue += 1
    division *= 2

print(white)
print(blue)
