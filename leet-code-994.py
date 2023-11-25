class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        drxn=[(1,0),(0,1),(0,-1),(-1,0)]
        n=len(grid)
        m=len(grid[0])
        q=deque() #row,col,time
        unrotten=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j,0))
                if grid[i][j]==1:
                    unrotten+=1
        change=0
        t=0
        while q:
            row,col,t=q.popleft()

            for x,y in drxn:
                nrow,ncol=x+row,y+col
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1:
                    q.append((nrow,ncol,t+1))
                    grid[nrow][ncol]=2
                    change+=1
        return t if change==unrotten else -1   
