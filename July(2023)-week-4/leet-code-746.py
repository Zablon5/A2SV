class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo={}
        n=len(cost)
        def rec(n):
            if n<2:
                return cost[n]
            if n in memo:
                return memo[n]   
            result=cost[n]+min(rec(n-1),rec(n-2)) 
            memo[n]=result
            return result 
        return min(rec(n-1),rec(n-2))     
