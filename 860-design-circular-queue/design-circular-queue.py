class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None]*k
        self.front = 0
        self.rear = 0
        self.size = 0
    def enQueue(self, value: int) -> bool:
        if(self.size == self.k):
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear+1)%self.k
        self.size+=1
        return True
    def deQueue(self) -> bool:
        if self.size == 0:
            return False
        self.front = (self.front+1)%self.k
        self.size-=1
        return True
    def Front(self) -> int:
        if not self.isEmpty():
            return self.queue[self.front]
        return -1
    def Rear(self) -> int:
        if not self.isEmpty():
            return self.queue[(self.rear-1)%self.k]
        return -1
    def isEmpty(self) -> bool:
        return (self.size == 0)

    def isFull(self) -> bool:
        return self.size == self.k


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()