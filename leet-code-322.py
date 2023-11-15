class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def rec(coins, target, i, dp):
            if target == 0:
                return 0
            if target < 0:
                return float('inf')
            if i >= len(coins):
                return float('inf')
            if (i,target) in dp:
                return dp[(i,target)]
            pick = 1 + rec(coins, target - coins[i], i, dp)
            not_pick = rec(coins, target, i + 1, dp)
            dp[(i,target)] = min(pick, not_pick)
            return min(pick,not_pick)
        
        dp ={}
        
        ans = rec(coins, amount, 0, dp)
        
        if ans == float('inf'):
            return -1
        else:
            return ans
