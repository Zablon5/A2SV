class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        mn=len(nums)+1
        l=0
        cu=0
        if sum(nums)<target:
            return 0
        for r in range(len(nums)):
            cu+=nums[r]
            while cu>=target:
                cu=cu-nums[l]
                mn=min(mn,r-l+1)
                l+=1
        return mn        
        
