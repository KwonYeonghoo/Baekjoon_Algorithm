N = int(input())
arr = [input() for _ in range(N)]

def recursion(str, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif str[l] != str[r]:
        return 0
    else:
        return recursion(str, l+1, r-1)

def isPalindrome(str):
    return recursion(str, 0, len(str)-1)

for word in arr:
    count = 0
    print(isPalindrome(word), count)