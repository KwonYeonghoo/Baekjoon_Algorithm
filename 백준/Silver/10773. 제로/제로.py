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
        
    def sum(self):
        if self.idx == 0:
            return 0
        sum = 0
        for i in range(self.idx):
            sum += self.arr[i]
        return sum
    
    def __str__(self):
        if self.idx == 0:
            return "빈 스택입니다."
        return str(self.arr[:self.idx])
    

K = int(input())

prompts = [int(input()) for _ in range(K)]

stack = Stack(100000)

for prompt in prompts:
    if prompt == 0:
        stack.pop()
    else:
        stack.push(prompt)

print(stack.sum())