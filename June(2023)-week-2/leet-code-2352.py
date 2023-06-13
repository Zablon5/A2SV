class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n=len(grid)
        def getcol(i):
            col=[]
            for j in range(n):
                col.append(grid[j][i])
            return col
        def getrow(i):
              
            return grid[i]    
        count=0
        for i in range(n):
            row=getrow(i)
            
            for j in range(n):
                col=getcol(j)
                mini=0
                for x in range(n):

                    if row[x]==col[x]:
                        mini+=1
                if mini==n:
                    count+=1
        
        return count    
