def solution(diffs, times, limit):
    
    # 이분탐색?
    # limit 안에 들면서 모든 문제를 해결할 수 있는 최소 level을 리턴하는 문제
    MAX_LEVEL = max(diffs)
    
    def calculate_time(level, diffs, times):
        total = 0
        diffs = [0] + diffs
        times = [0] + times
        
        for i in range(1, len(diffs)):
            if diffs[i] <= level:
                total += times[i]
            else:
                total += (diffs[i] - level) * (times[i] + times[i-1]) + times[i]
        return total
        
    def binary_search(k):
        left, right = 0, MAX_LEVEL
        while left + 1 < right:
            mid = (left + right) // 2
            if calculate_time(mid, diffs, times) <= k:
                right = mid
            else:
                left = mid
        return right
    
    answer = binary_search(limit)
    
    return answer