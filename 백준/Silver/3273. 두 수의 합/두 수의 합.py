n = int(input())
arr = list(map(int, input().split()))
x = int(input())

MAX = 1000000
def find_matches(arr, x):
    count = 0
    count_arr = [0] * (MAX+1)
    
    for num in arr:
        count_arr[num] = 1
        
        if x - num >= MAX:
            continue
        elif x <= num:
            continue
        else:
            if x / 2 == num:
                continue
            elif count_arr[x-num]==1:
                count+=1
            else:
                continue
    return count

print(find_matches(arr, x))