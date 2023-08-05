class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp={}
        for i in arr:
            if dp.get(i-difference,-1)==-1:
                dp[i]=0
            else:
                dp[i]=dp[i-difference]+1
        return max(dp.values())+1          
