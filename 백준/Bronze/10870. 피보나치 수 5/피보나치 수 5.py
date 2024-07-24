N = int(input())

##### top down(재귀) #####
# dp 테이블 생성(-1로 초기화)
dp = [-1] * (N+1)

def fibo(x):
    # 탈출 조건
    if x==0 :
        return 0
    elif x==1 :
        return 1
    # 이미 dp테이블에 값이 있는 경우
    elif dp[x] != -1:
        return dp[x]
    # dp테이블에 값이 없는 경우
    else:
        dp[x] = fibo(x-2) + fibo(x-1)
        return dp[x]
    
print(fibo(N))