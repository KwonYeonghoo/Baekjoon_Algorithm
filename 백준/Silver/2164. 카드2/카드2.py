class Queue:
    def __init__(self, max_size=1000000):
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
    
    def __str__(self):
        return str(self.dat)
    
# 1. pop
# 2. head -> tail
# 3. size == 1 이 되면 break

N = int(input())

queue = Queue()

for i in range(1, N+1):
    queue.push(i)

while queue.size() >= 2:
    queue.pop()
    # print(queue.head, queue.tail)
    temp = queue.front()
    queue.pop()
    queue.push(temp)
    # print(queue.head, queue.tail)

print(queue.front())