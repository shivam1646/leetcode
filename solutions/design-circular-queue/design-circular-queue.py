class MyCircularQueue:

    # initialize queue with given size
    def __init__(self, k: int):
        self.queue = [None] * k
        self.size = k
        self.rear = -1
        self.front = -1

    def enQueue(self, value: int) -> bool:
        # queue is full so can't insert
        if self.isFull(): return False
        # insert element at the next available empty position
        # e.g. [1, 2, 3, _]
        # front = 0, rear = 2, size = 4. new rear = (2 + 1) % 4 = 3
        # e.g. [_, 2, 3, 4]
        # front = 1, rear = 3, size = 3. new rear = (3 + 1) % 4 = 0
        self.rear = (self.rear + 1) % self.size
        if self.front == -1: self.front += 1
        self.queue[self.rear] = value
        return True

    def deQueue(self) -> bool:
        # queue is empty so can't remove 
        if self.isEmpty(): return False
        if self.front == self.rear:
            # if queue will become empty after removing current item
            self.front = -1
            self.rear = -1
        else:
            # increment front ptr
            self.front = (self.front + 1) % self.size
        return True

    def Front(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.front]

    def Rear(self) -> int:
        return -1 if self.isEmpty() else self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.front == -1 and self.rear == -1

    def isFull(self) -> bool:
        return (self.rear + 1) % self.size == self.front


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
