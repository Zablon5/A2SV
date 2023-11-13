class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums))
       
        def rec(nums,i,dp):
            if i==0:
                return nums[i]
            if i<0:
                return 0    
            print(dp)  
            if dp[i]!=-1:
                return dp[i]  
            pick=nums[i]+rec(nums,i-2,dp)
            not_pick=0+rec(nums,i-1,dp)
            dp[i]=max(pick,not_pick)
            return dp[i]
        
        return rec(nums,len(nums)-1,dp)
   
        