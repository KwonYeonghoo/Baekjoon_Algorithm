def solution(info, n, m):
    
    dp = [[float('inf')]*m for _ in range(len(info)+1)]
    dp[0][0] = 0 # 초기값 세팅
    
    for i in range(len(info)):
        for b in range(m):
            if dp[i][b] == float('inf'):
                continue
            
            # 1) A가 도둑
            if dp[i][b] + info[i][0] < n:
                dp[i+1][b] = min(dp[i+1][b], dp[i][b] + info[i][0])
            
            # 2) B가 도둑
            if info[i][1] + b < m:
                dp[i+1][info[i][1] + b] = min(dp[i][b], dp[i+1][info[i][1] + b])
    
            
    return min(dp[-1]) if min(dp[-1]) != float('inf') else -1