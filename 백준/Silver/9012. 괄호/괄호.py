import sys

N = int(input())

def is_vps(string):
    stack = []
    for w in string:
        if w == "(":
            stack.append(w)
        if w == ")":
            if len(stack) == 0:
                return False
            top = stack.pop()
            
    if len(stack) == 0:
        return True
    else: return False

for _ in range(N):
    if is_vps(input()):
        print("YES")
    else: print("NO")