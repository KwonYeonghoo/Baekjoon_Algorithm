import sys

# 1. 소괄호 짝 이루기
# 2. 대괄호 짝 이루기
# 3. 괄호 사이의 문자열도 균형을 이뤄야함
# 4. 괄호가 아예 없는 경우도 균형을 이룸

pair = {"]": "[", ")": "("}


def is_balanced(sentence):
    """
    1. 왼쪽 괄호 등장하면 스택에 push
    2. 오른쪽 괄호 등장하면 스택에서 pop
        2-1. 오른쪽 괄호 등장했을 때 스택 상단에 짝이 맞는 괄호가 없으면 return False
    3. 스택에 남는 왼쪽 괄호가 있으면 return False

    Args:
        str_ (str): 입력으로 들어오는 문장
    """
    stack = []
    for w in sentence:
        if (w == "(") or (w == "["):
            stack.append(w)
        if (w == ")") or (w == "]"):
            if len(stack) == 0:
                return False
            top = stack.pop()
            if pair[w] != top:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


while True:
    input_str = input()
    if input_str == ".":
        break
    if is_balanced(input_str):
        print("yes")
    else:
        print("no")
