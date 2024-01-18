class Solution:
    def climbStairs(self, n: int) -> int:
        memo={}
        def rec(n,memo):
            if n==1:
               return 1
            if n==2:
                return 2   
            if n in memo:
                    return memo[n]
            else:
                
                memo[n]=rec(n-1,memo)+rec(n-2,memo)
                return memo[n]
        
        return rec(n,memo) 