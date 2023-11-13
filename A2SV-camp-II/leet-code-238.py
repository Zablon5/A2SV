class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n
        prepro=1
        for i in range(n):
            res[i]*=prepro
            prepro*=nums[i]
        pospro=1
        for i in reversed(range(n)):
            res[i]*=pospro
            pospro*=nums[i]
        return res    
