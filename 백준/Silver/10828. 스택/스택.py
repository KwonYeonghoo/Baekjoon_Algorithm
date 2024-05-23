class Stack:
    def __init__(self, length):
        self.length = length
        self.arr = [0 for _ in range(length)]
        self.idx = 0
        
    def push(self, data):
        if self.idx < self.length:
            self.arr[self.idx] = data
            self.idx += 1

    def pop(self):
        if self.idx == 0: 
            return -1
        self.idx -= 1
        return self.arr[self.idx] # pop한 값 반환

    def top(self):
        if self.idx == 0: 
            return -1
        return self.arr[self.idx - 1]
    
    def empty(self):
        if self.idx == 0:
            return 1
        else:
            return 0
    
    def __str__(self):
        if self.idx == 0:
            return "빈 스택입니다."
        return str(self.arr[:self.idx])
    
# stack = stack.Stack(10000)
stack = Stack(10000)

n = int(input())

prompts = [input().split() for _ in range(n)]

for prompt in prompts:
    if prompt[0] == 'push':
        stack.push(prompt[1])
    elif prompt[0] == 'pop':
        print(stack.pop())
    elif prompt[0] == 'size':
        print(stack.idx)
    elif prompt[0] == 'empty':
        print(stack.empty())
    else:
        print(stack.top())