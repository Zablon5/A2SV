class DataStream:

    def __init__(self, value: int, k: int):
        self.value=value
        self.k=k
        self.dq=deque()

    def consec(self, num: int) -> bool:
        while self.dq and self.dq[-1]!=num:
            self.dq.pop()
        self.dq.append(num) 
        if num!=self.value:
            return False
        return len(self.dq)>=self.k
                
          


        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
