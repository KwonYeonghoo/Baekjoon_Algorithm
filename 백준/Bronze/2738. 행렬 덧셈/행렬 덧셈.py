N,M = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
X = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        X[i][j] = str(A[i][j] + B[i][j])

for row in X:
    print(" ".join(row))