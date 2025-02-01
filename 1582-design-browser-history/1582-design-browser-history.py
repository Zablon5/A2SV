class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.back = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
       
    def visit(self, url: str) -> None:
        newNode = Node(url)
        self.head.next = newNode
        newNode.back = self.head
        self.head = self.head.next


    def back(self, steps: int) -> str:
        count = 0
       
        
        while self.head and self.head.back:
            
            count += 1
            if count == steps:
                self.head = self.head.back
                return self.head.val
            self.head = self.head.back
        
        return self.head.val
       

    def forward(self, steps: int) -> str:
        count = 0
        
        while self.head and self.head.next:
            
            count += 1
            if count == steps:
                self.head = self.head.next
                return self.head.val
            self.head = self.head.next
        
        return self.head.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)