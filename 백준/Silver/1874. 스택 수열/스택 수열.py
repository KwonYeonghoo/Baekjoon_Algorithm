import sys

# push하다가 stack의 top과 push한 횟수가 같으면 pop
# push 횟수보다 작은 숫자가 나오면 pop
# push 횟수가 n번이 되면 스택에 남은 수 모두 pop

n = int(input())
arr = [int(input()) for _ in range(n)]

stack = []
push_count = 0
result = []
flag = True

for num in arr:
    # 필요한 숫자가 나올 때까지 push
    while push_count < num:
        push_count += 1
        stack.append(push_count)
        result.append("+")

    # 스택의 top이 원하는 숫자인 경우 pop
    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        # 스택의 top이 원하는 숫자가 아니면 불가능한 경우
        flag = False
        break

if flag:
    print("\n".join(result))
else:
    print("NO")
