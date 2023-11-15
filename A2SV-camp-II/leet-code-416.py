class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sm=sum(nums)
        if sm%2:
            return False
        def rec(i,target,dp):
            if (i,target) in dp:
                return dp[(i,target)]
            if target==0:
                return True
            if i>=len(nums):
                return False
                
            pick=rec(i+1,target-nums[i],dp)    
            unpick=rec(i+1,target,dp)
            dp[(i,target)]=pick or unpick   
            return pick or unpick
        dp={}    
        return rec(0,sm//2,dp)  
