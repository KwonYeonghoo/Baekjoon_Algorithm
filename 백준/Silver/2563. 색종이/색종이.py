N = int(input())
paper = [[0 for _ in range(100)] for _ in range(100)]
colors = [list(map(int, input().split())) for _ in range(N)]
minus = 0
for color in colors:
    for row in range(color[1], color[1]+10):
        for col in range(color[0], color[0]+10):
            if paper[row][col] == 1:
                minus += 1
                continue
            paper[row][col] = 1
print(100*N - minus)