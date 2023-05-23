class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh=0
        queue=deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    queue.append([i,j])
                elif grid[i][j]:
                    fresh+=1
        t=0
        drxn=[[0,1],[-1,0],[1,0],[0,-1]]

        while queue and fresh:
            for i in range(len(queue)):
                r,c=queue.popleft()
                for x,y in drxn:
                    row,col=r+x,c+y
                    if (row<0 or row==len(grid) or col<0 or col==len(grid[0]) or grid[row][col]!=1):
                        continue
                    grid[row][col]=2    
                    queue.append([row,col])   
                    fresh-=1
            t+=1
        return t if fresh==0 else -1             
