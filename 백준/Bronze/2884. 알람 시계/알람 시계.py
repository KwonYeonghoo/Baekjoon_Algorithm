# 알람 맞추기
# H : M

# 케이스 1) M이 45보다 작을 경우
## H를 1 빼고 M에 60을 더해준다
## 근데 여기서 H가 0이었을 경우 H를 23으로 수정

# 케이스 2) M이 45 이상일 경우
## 그냥 M에서 45를 빼준다

H, M = list(map(int, input().split()))
if M < 45:
    if H == 0:
        H = 23
        M = M + 60 - 45
    else:
        H -= 1
        M = M + 60 - 45
else:
    M -= 45
print(f"{H} {M}")