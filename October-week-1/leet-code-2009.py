class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n=len(nums)
        ans=n
        nums=sorted(set(nums))
        r=0
        for l in range(len(nums)):
            while r<len(nums) and nums[r]<nums[l]+n:
                r+=1
            w=r-l
            ans=min(ans,n-w)    
        return ans  
