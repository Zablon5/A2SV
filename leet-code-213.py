class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        dp1=[-1]*(len(nums)-1)
        dp2=[-1]*(len(nums)-1)
        def rec(nums,i,dp):
            if dp[i]!=-1:
                return dp[i]
            if i==0:
                return nums[0]
            if i<0:
                return 0    
            pick=nums[i]+rec(nums,i-2,dp)
            not_pick=0+rec(nums,i-1,dp)
            dp[i]=max(pick,not_pick)
            return dp[i]
        return max(rec(nums[:len(nums)-1],len(nums)-2,dp1),rec(nums[1:],len(nums)-2,dp2))
