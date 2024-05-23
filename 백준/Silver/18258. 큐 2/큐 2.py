class Queue:
    def __init__(self, max_size=2000000):
        self.dat = [0] * max_size
        self.head = 0
        self.tail = 0

    def push(self, x):
        self.dat[self.tail] = x
        self.tail += 1

    def pop(self):
        if self.head == self.tail:
            return -1
        self.head += 1
        return self.dat[self.head-1]

    def front(self):
        if self.head == self.tail:
            return -1
        return self.dat[self.head]

    def back(self):
        if self.head == self.tail:
            return -1
        return self.dat[self.tail - 1]
    
    def size(self):
        return self.tail - self.head
    
    def empty(self):
        if self.head == self.tail:
            return 1
        return 0
    
    
N = int(input())

queue = Queue()

prompts = [input().split() for _ in range(N)]
for prompt in prompts:
    if prompt[0] == "push":
        queue.push(prompt[1])
    elif prompt[0] == "front":
        print(queue.front())
    elif prompt[0] == "back":
        print(queue.back())
    elif prompt[0] == "size":
        print(queue.size())
    elif prompt[0] == "pop":
        print(queue.pop())
    elif prompt[0] == "empty":
        print(queue.empty())
        