class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def rec(n,m,dp):
            if m==1 and n==1:
                return 1
            if m<0 or n<0:
                return 0
            if (n,m) in dp:
                return dp[(n,m)]   
            left=rec(n-1,m,dp)
            right=rec(n,m-1,dp) 
            dp[(n,m)]=right+left
            return right+left
        dp={}     
        return rec(n,m,dp) 
