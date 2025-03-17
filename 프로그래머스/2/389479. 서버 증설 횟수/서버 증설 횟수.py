def solution(players, m, k):
    answer = 0
    live_server = [0] * 24
    
    for i in range(24):
        if players[i] < m:
            continue
        server_needed = (players[i] - m) // m + 1
        server_needed -= live_server[i]
        
        if server_needed > 0:
            answer += server_needed
            for j in range(i, i+k):
                if j < 24:
                    live_server[j] += server_needed
        
    return answer