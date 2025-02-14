import sys
input = sys.stdin.readline

# 방향 벡터 (상, 우, 하, 좌)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def OOB(nx, ny):
    return nx < 0 or ny < 0 or nx >= N or ny >= M

N, M = map(int, input().strip().split())
arr = [list(map(int, input().strip().split())) for _ in range(N)]
max_size = 0
visited = [[False] * M for _ in range(N)]  # DFS 방문 배열

def dfs(x, y, depth, total):
    """DFS를 이용하여 4칸짜리 테트로미노 탐색"""
    global max_size

    # 가지치기: 현재 합이 이미 max_size보다 작으면 탐색할 필요 없음
    if total + (4 - depth) * max_val <= max_size:
        return

    if depth == 4:
        max_size = max(max_size, total)
        return

    for d in range(4):
        nx, ny = x + dx[d], y + dy[d]
        if OOB(nx, ny) or visited[nx][ny]:
            continue
        visited[nx][ny] = True
        dfs(nx, ny, depth + 1, total + arr[nx][ny])
        visited[nx][ny] = False  # 백트래킹

def check_t_shape(x, y):
    """ㅗ, ㅜ, ㅓ, ㅏ 모양을 검사"""
    global max_size
    for case in [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],  # ㅗ
        [(0, 0), (0, -1), (0, 1), (1, 0)],  # ㅜ
        [(0, 0), (0, -1), (-1, 0), (1, 0)],  # ㅏ
        [(0, 0), (0, -1), (-1, 0), (0, 1)],  # ㅓ
    ]:
        total = 0
        valid = True
        for dx, dy in case:
            nx, ny = x + dx, y + dy
            if OOB(nx, ny):
                valid = False
                break
            total += arr[nx][ny]
        if valid:
            max_size = max(max_size, total)

# 배열 내 최댓값 구하기 (가지치기에 사용)
max_val = max(map(max, arr))

# 모든 위치에서 탐색
for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])  # DFS 탐색
        visited[i][j] = False
        check_t_shape(i, j)  # ㅗ, ㅜ, ㅓ, ㅏ 모양 체크

print(max_size)