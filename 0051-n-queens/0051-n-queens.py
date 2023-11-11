class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]*n for _ in range(n)]
        ans=[]
        leftrow=[0]*n
        upperdiag=[0]*(2*n-1)
        lowerdiag=[0]*(2*n-1)
        print(board)
                               
        def solve(col,board,ans,n,leftrow,upperdiag,lowerdiag):
            if col==n:

                ans.append([''.join(row) for row in board])
                return
                
            for row in range(n):
                if leftrow[row]==0 and lowerdiag[row+col]==0 and upperdiag[n-1+col-row]==0: 
                    board[row][col]='Q'
                    leftrow[row]=1
                    lowerdiag[row+col]=1
                    upperdiag[n-1+col-row]=1

                    solve(col+1,board,ans,n,leftrow,upperdiag,lowerdiag)
                    board[row][col]='.'
                    leftrow[row]=0
                    lowerdiag[row+col]=0
                    upperdiag[n-1+col-row]=0
        solve(0,board,ans,n,leftrow,upperdiag,lowerdiag)    
        return ans  
        