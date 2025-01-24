import sys

N, M = map(int, input().split())
arr = list(map(int, sys.stdin.readline().strip().split()))
count = 0
prefix_sum = 0
prefix_mod = [0] * M  # M으로 나눈 나머지가 같은 것들의 개수를 저장

for num in arr:
    prefix_sum += num  # 누적합 계산
    mod = prefix_sum % M  # M으로 나눈 나머지 계산
    if mod == 0:  # 나머지가 0인 경우는 바로 카운트 증가
        count += 1
    prefix_mod[mod] += 1  # 나머지 값의 개수 증가

for n in prefix_mod:
    count += n * (n - 1) // 2
    # 나머지가 같은 것들의 개수가 n개라면 nC2의 경우의 수가 존재한다.
    # 이 경우의 수는 n(n-1)/2이다.
    # 이는 나머지가 같은 것들을 두개씩 뽑는 경우의 수이다.
    # 이 경우의 수를 더해준다.
    # 예를 들어 나머지가 1인 것이 3개 있다면 3C2의 경우의 수가 존재한다.
    # 이 경우의 수는 3이다.
    # 이 경우의 수를 더해준다.
    # 나머지가 같은 것들의 개수가 1개라면 경우의 수가 존재하지 않는다.
    # 따라서 더해줄 필요가 없다.
    # 나머지가 같은 것들의 개수가 0개라면 경우의 수가 존재하지 않는다.
    # 따라서 더해줄 필요가 없다.
    # 따라서 나머지가 같은 것들의 개수가 2개 이상인 것들만 경우의 수를 더해준다.
print(count)