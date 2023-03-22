class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        

    def sumRange(self, left: int, right: int) -> int:
        self.sum=0
        while left<=right:
            self.sum+=self.nums[left]
            left+=1
        return self.sum    
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
