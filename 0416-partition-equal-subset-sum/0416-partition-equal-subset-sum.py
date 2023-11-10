class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        n=len(nums)
        s=sum(nums)
        if s%2:
            return False
        dp = [[-1 for i in range(s//2 + 1)] for j in range(n+1)]

        def solve(ind , target):
            if target == 0: return True

            if ind == n-1 : return target == nums[ind]         # !!!!!!!
            
            if dp[ind][target] != -1: return dp[ind][target] 
            not_take = solve( ind+1 , target )

            take = False
            if target >= nums[ind]:
                take = solve( ind+1 , target-nums[ind] )

            dp[ind][target] = take or not_take
            return dp[ind][target]
        
        return solve(0 , s//2)
        