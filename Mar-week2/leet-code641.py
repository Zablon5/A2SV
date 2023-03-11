class MyCircularDeque:
    def __init__(self, k: int):
        self.k = k
        self.q = [0] * k
        self.head = 0
        self.tail = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.head = (self.head - 1) % self.k
        self.q[self.head] = value
        self.size += 1
        return True
        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail + 1) % self.k
        self.size += 1
        return True
        
    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.head = (self.head + 1) % self.k
        self.size -= 1
        return True
        
    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.tail = (self.tail - 1) % self.k
        self.size -= 1
        return True
        
    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[self.head]
        
    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.q[(self.tail - 1) % self.k]
        
