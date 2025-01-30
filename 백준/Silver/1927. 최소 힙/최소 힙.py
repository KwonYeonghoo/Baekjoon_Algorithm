import sys

# sys.stdin = open("/Users/hoo/Hoo/Study/알고리즘/2025/input.txt", "r")


# 최소 힙
class MinHeap:
    def __init__(self):
        self.heap = []

    def _parent(self, index):
        return (index - 1) // 2

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def push(self, value):
        """값을 최소힙에 추가"""
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, index):
        """새로운 요소가 추가될 때 최소힙 속성을 유지하도록 조정"""
        while index > 0 and self.heap[index] < self.heap[self._parent(index)]:
            self.heap[index], self.heap[self._parent(index)] = (
                self.heap[self._parent(index)],
                self.heap[index],
            )
            index = self._parent(index)

    def pop(self):
        """최소값을 제거하고 반환"""
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, index):
        """루트 요소 제거 후 힙 속성을 유지하도록 조정"""
        size = len(self.heap)
        while True:
            smallest = index
            left = self._left_child(index)
            right = self._right_child(index)

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == index:
                break

            self.heap[index], self.heap[smallest] = (
                self.heap[smallest],
                self.heap[index],
            )
            index = smallest

    def peek(self):
        return self.heap[0] if self.heap else None


#####################################################
import heapq

# heapq.heappush(heap, item): 힙에 item 추가
# heapq.heappop(item): 힙에서 최소값 제거 후 반환
# heapq.heapify(iterable): 리스트를 최소힙으로 변환
# heapq.heappushpop(heap, item): item을 넣고, 가장 작은 요소를 제거 후 반환


N = int(input())

heap = MinHeap()
for _ in range(N):
    num = int(sys.stdin.readline().strip())
    if num == 0:
        if len(heap.heap) == 0:
            print(0)
        else:
            print(heap.pop())
    else:
        heap.push(num)