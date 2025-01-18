import sys


# 1. 산술평균
def get_average(sorted_arr):
    return round(sum(sorted_arr) / len(sorted_arr))


# 2. 중앙값
def get_median(sorted_arr):
    middle_idx = len(sorted_arr) // 2
    return sorted_arr[middle_idx]


# 3. 최빈값
def get_mode(count_arr):
    max_val_idx = -1
    max_val = -10000
    second_small = 0
    for i in range(len(count_arr)):
        if count_arr[i] > max_val:
            max_val = count_arr[i]
            max_val_idx = i
            second_small = 0
        elif count_arr[i] == max_val:
            if count_arr[i] == 0:
                continue
            if second_small < 1:
                max_val_idx = i
                second_small += 1
    return max_val_idx - 4000


# 4. 범위
def get_range(sorted_arr):
    return sorted_arr[-1] - sorted_arr[0]


N = int(input())
sorted_arr = sorted([int(sys.stdin.readline().strip()) for _ in range(N)])
count_arr = [0] * 8001
for val in sorted_arr:
    count_arr[val + 4000] += 1

print(get_average(sorted_arr))
print(get_median(sorted_arr))
print(get_mode(count_arr))
print(get_range(sorted_arr))
