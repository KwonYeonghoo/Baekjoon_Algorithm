# 숫자 10개 입력
# 42로 나눈 나머지, 다른 값 몇 개 있는지

arr = [int(input()) % 42 for _ in range(10)]

leftover = [0] * 42

for num in arr:
    leftover[num] += 1

print(42 - leftover.count(0))