class Queue:
    def __init__(self, N):
        self.queue = [0] * (N + 1)
        self.left = -1
        self.right = -1

    def push(self, x):
        self.right += 1
        self.queue[self.right] = x

    def pop(self):
        if self.left == self.right:
            return -1
        self.left += 1
        return self.queue[self.left]

    def size(self):
        return self.right - self.left

    def empty(self):
        return int(self.right == self.left)

    def front(self):
        if self.left == self.right:
            return -1
        return self.queue[self.left + 1]

    def back(self):
        if self.left == self.right:
            return -1
        return self.queue[self.right]


N = int(input())
q = Queue(N)

for _ in range(N):
    cmd = input().split()
    if len(cmd) == 2:
        q.push(int(cmd[1]))
    else:
        if cmd[0] == "pop":
            print(q.pop())
        elif cmd[0] == "size":
            print(q.size())
        elif cmd[0] == "empty":
            print(q.empty())
        elif cmd[0] == "front":
            print(q.front())
        elif cmd[0] == "back":
            print(q.back())