class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def rec(i,amount,target,dp):
            if (i,amount) in dp:
                return dp[(i,amount)]
            if i>=len(nums):
                if target==amount:
                    return 1
                return 0
            addition=rec(i+1,amount+nums[i],target,dp)    
            subtract=rec(i+1,amount-nums[i],target,dp)
            dp[(i,amount)]=addition+subtract
            return addition+subtract
        dp={}    
        return rec(0,0,target,dp) 
