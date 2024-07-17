n, m = map(int, input().split())
arr = [[c for c in input()] for _ in range(n)]

    
def get_minimum_count(chess_board):
    cnt = 0
    # print(chess_board)
    for r in range(8):
        for c in range(8):
            # 짝수일 경우
            if (r+c) % 2 == 0 and chess_board[r][c] != "W":
                cnt += 1
            elif (r+c) % 2 == 1 and chess_board[r][c] != "B":
                cnt += 1
            else:
                continue
    if cnt > 32:
        cnt = 64 - cnt
    
    return cnt

# 왼쪽 상단 노드 좌표 [i,j]
count = []
for i in range(n-8+1):
    for j in range(m-8+1):
        chess_board = [row[j:j+8] for row in arr[i:i+8]]
        count.append(get_minimum_count(chess_board))

print(min(count))