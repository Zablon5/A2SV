class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m=len(grid)
        n=len(grid[0])

        drxn=[(0,1),(1,0),(-1,0),(0,-1)]
        visited=[[0 for _ in range(n)] for _ in range(m)]
        def dfs(row,col):
            for x,y in drxn:
                nr,nc=row+x,col+y
                if 0<=nr<m and 0<=nc<n and not visited[nr][nc] and grid[nr][nc]=='1':
                    visited[nr][nc]=1
                    dfs(nr,nc)

        ans=0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j]=='1':
                    visited[i][j]=1
                    ans+=1
                    dfs(i,j)
        return ans
