class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            pick=nums[i]
            if i>1:
                pick+=dp[i-2]
            not_pick=0+dp[i-1]
            dp[i]=max(pick,not_pick)
        print(dp)    
        return dp[len(nums)-1]    

       
       
   
        