class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        rsum=sum(nums)
        lsum=0
        for i,val in enumerate(nums):
            rsum-=val
            if rsum==lsum:
                return i
            else:
                lsum+=val
        return -1  
