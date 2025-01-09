L = int(input())
arr = input()

# print(ord("a")) # 97
r, M = 31, 1234567891

result = 0
for i in range(L):
    a = ord(arr[i]) - 96
    result += a * r ** i

print(result % M)