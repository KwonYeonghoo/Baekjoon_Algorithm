N = int(input())
arr = list(map(int, input().split()))
v = int(input())

# print(arr.count(v))

new_arr = [0] * 201

for n in arr:
    new_arr[n+100] += 1
    
print(new_arr[v+100])