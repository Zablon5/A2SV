class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        visited=[[0 for _ in range(m)] for _ in range(n)]
        drxn=[(1,0),(0,1),(-1,0),(0,-1)]
        
        for i in range(m):
            if grid[0][i]==1:
                q.append((0,i))
                visited[0][i]=1
            if grid[n-1][i]==1:
                q.append((n-1,i))
                visited[n-1][i]=1
             
        for i in range(n):
            if grid[i][0]==1:
                q.append((i,0))
                visited[i][0]=1
            if grid[i][m-1]==1:
                q.append((i,m-1))  
                visited[i][m-1]=1  
    
        while q:
            r,c=q.popleft()
            for x,y in drxn:
                row,col=x+r,c+y
                if 0<=row<n and 0<=col<m and not visited[row][col] and grid[row][col]==1:
                    visited[row][col]=1
                    q.append((row,col))
        init_land=0            
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]==0:
                    init_land+=1
        return init_land
