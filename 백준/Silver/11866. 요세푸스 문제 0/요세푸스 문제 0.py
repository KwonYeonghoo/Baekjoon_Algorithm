N, K = map(int, input().split())

arr = [i for i in range(1, N + 1)]

idx = 0
result = []

while arr:
    idx = (idx + K - 1) % len(arr)  # K번째 사람의 인덱스 계산
    result.append(arr.pop(idx))  # 해당 인덱스의 요소 제거 후 result에 추가

print(f"<{', '.join(map(str, result))}>")