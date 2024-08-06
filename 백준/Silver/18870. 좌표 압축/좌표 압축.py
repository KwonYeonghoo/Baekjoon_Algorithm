N = int(input())

# N의 최댓값이 100만이기 때문에, O(N^2) 불가능

arr = list(map(int, input().split())) # 정렬시키기
sorted_arr = sorted(arr)
# 경계값을 1씩 높여가며 좌측에 존재하는 수의 개수 세기
count = {}
count[sorted_arr[0]] = 0
bound = 0
for i in range(1,N):
    if sorted_arr[i-1] == sorted_arr[i]:
        continue
    bound += 1
    count[sorted_arr[i]] = bound

for a in arr:
    print(count[a], end=' ')