n = int(input())
arr = [input().split(' ') for _ in range(n)]

for words in arr:
    A = sorted(words[0])
    B = sorted(words[1])
    
    if A == B:
        print("Possible")
    else:
        print("Impossible")