import sys

N, r, c = map(int, input().split())

# 큰 문제를 작은 문제로 쪼개서 푸는 문제
# 분할정복 --> 재귀
# 가로세로 각 한 번씩 분할하는 것을 재귀적으로 호출
# 길이가 1이 될 때까지

# 전역변수 선언
count = 0

# 00 02 20 22
# 00 04 40 44


def recursion(x, y, n):  # n은 지수
    global count
    if n == 1:
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                count += 1
                # print(i, j, count)
                if i == r and j == c:
                    print(count - 1)
        return

    size = 2 ** (n - 1)

    if r < x + size and c < y + size:
        recursion(x, y, n - 1)
    elif r < x + size and c >= y + size:
        count += size**2
        recursion(x, y + size, n - 1)
    elif r >= x + size and c < y + size:
        count += 2 * size**2
        recursion(x + size, y, n - 1)
    else:
        count += 3 * size**2
        recursion(x + size, y + size, n - 1)


recursion(0, 0, N)
