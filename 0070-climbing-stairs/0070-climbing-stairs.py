class Solution:
    def climbStairs(self, n: int) -> int:

        def Climb(n, memo):
            if n == 0:
                return 1
            if n < 0:
                return 0
            if n in memo:
                return memo[n]
            singleSteps = Climb(n-1, memo)
            twoSteps = Climb(n-2, memo)
            
            memo[n] = singleSteps + twoSteps
            return singleSteps + twoSteps
        memo = {}
        Climb(n,memo)
        return memo[n]