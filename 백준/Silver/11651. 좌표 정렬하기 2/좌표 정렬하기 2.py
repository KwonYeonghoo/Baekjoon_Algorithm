N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
sorted_arr = sorted(arr, key = lambda x: (x[1], x[0]))

for val in sorted_arr:
    print(" ".join(map(str, val)))