class Stack:
    def __init__(self, length):
        self.length = length
        self.arr = [0 for _ in range(length)]
        self.index = 0
        self.size = self.index
        
    # push, pop, top, empty, size
    def push(self, data):
        if self.index < self.length:
            self.arr[self.index] = data
            self.index += 1
    
    def pop(self):
        if self.index == 0:
            return -1
        self.index -= 1
        return self.arr[self.index]
    
    def top(self):
        if self.index == 0:
            return -1
        return self.arr[self.index-1]
    
    def isEmpty(self):
        if self.index == 0:
            return 1
        else:
            return 0
        
    def __str__(self):
        if self.index == 0:
            return "빈 스택입니다."
        return f"스택: {self.arr[:self.index]}"
    
def check_pelindrome(num):
    ans = 'yes'
    n_len = len(num)
    # num의 길이가 홀수인 경우
    if n_len % 2 == 1:
        stack = Stack(n_len // 2)
        # stack에 push
        for n in num[:stack.length]:
            stack.push(n)
        # 하나씩 pop하며 숫자 비교
        for n in num[stack.length+1:]:
            if stack.pop() == n:
                pass
            else:
                ans = 'no'
    # num의 길이가 짝수인 경우
    else:
        stack = Stack(n_len // 2)
        for n in num[:stack.length]:
            stack.push(n)
        for n in num[stack.length:]:
            if stack.pop() == n:
                pass
            else:
                ans = 'no'
    return ans
    
arr = []
while True:
    num = input()
    if num == '0':
        break
    arr.append(check_pelindrome(num))

print("\n".join(arr))