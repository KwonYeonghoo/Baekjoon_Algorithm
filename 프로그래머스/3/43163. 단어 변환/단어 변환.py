from collections import deque

def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    Q = deque([(begin, 0)])
    # 딱 한 글자만 다른 단어 찾기
    # 찾은 단어를 visited 처리하고, Q에 추가
    
    def get_one_different(t, w):
        count = 0
        for i in range(len(t)):
            if t[i] != w[i]:
                count += 1
        if count == 1:
            return True
        else: return False
    
    while Q:
        x, depth = Q.popleft()
        for i in range(len(words)):
            if visited[i] != 0:
                continue
            if get_one_different(x, words[i]):
                visited[i] = depth + 1
                Q.append((words[i], depth + 1))
    try:
        return visited[words.index(target)]
    except:
        return 0