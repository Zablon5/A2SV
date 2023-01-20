class MinStack:

    def __init__(self):
        self.stack=deque()
        self.min=deque()
        

    def push(self, val: int) -> None:
        if len(self.stack)>0:
            if (val<=self.min[-1]):
                self.min.append(val)
                self.stack.append(val)
            else:
                self.stack.append(val)    
        else:
            self.stack.append(val)
            self.min.append(val)
        

    def pop(self) -> None:
        if len(self.stack)>0 and len(self.min)>0:
            if self.stack[-1]==self.min[-1]:
                self.min.pop()

           
        self.stack.pop()    
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if len(self.min)>0:
            return self.min[-1]
        else:
            return 0    
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
