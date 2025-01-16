# push X, pop, size, empty, top
N = int(input())


class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, x):
        self.stack.append(x)
        self.size += 1

    def pop(self):
        if self.isempty():
            return -1
        self.size -= 1
        return self.stack.pop()

    def isempty(self):
        return int(self.size == 0)

    def top(self):
        if self.isempty():
            return -1
        return self.stack[-1]


s = Stack()

for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        s.push(int(cmd[1]))
    else:
        if cmd[0] == "top":
            print(s.top())
        elif cmd[0] == "size":
            print(s.size)
        elif cmd[0] == "pop":
            print(s.pop())
        else:
            print(s.isempty())