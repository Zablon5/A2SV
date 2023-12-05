class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        n=len(nums)
        pre=1
        suf=1
        mx=0
        if n==1:
            return nums[0]
        for i in range(n):
            if pre==0: pre=1
            if suf==0: suf=1
            pre*=nums[i]
            suf*=nums[n-1-i]
            mx=max(pre,suf,mx)
        return mx
