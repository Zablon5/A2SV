class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         # Create a 2D array dp with all values initialized to 0
        dp = [[0] * n for _ in range(m)]

        # Initialize the leftmost column and topmost row to 1
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        # Fill in the dp array using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        # The value in the bottom-right corner represents the number of unique paths
        return dp[m - 1][n - 1]
        
