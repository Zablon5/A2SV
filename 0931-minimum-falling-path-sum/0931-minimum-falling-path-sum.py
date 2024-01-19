class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        def rec(i,j,dp):
            if j>=len(matrix[0]) or j<0:
                return float('inf')
            if i==n-1 :
                return matrix[i][j]
        
            if (i,j) in dp:
                return dp[(i,j)]
            
        
            below=matrix[i][j]+rec(i+1,j,dp)  
            left_diag=matrix[i][j]+rec(i+1,j-1,dp)
            right_diag=matrix[i][j]+rec(i+1,j+1,dp)
            dp[(i,j)]=min(below,left_diag,right_diag)
            return min(below,left_diag,right_diag)  
        mini=float('inf') 
        dp={}   
        for k in range(len(matrix[0])):
            mini=min(mini,rec(0,k,dp))
        return mini    
        