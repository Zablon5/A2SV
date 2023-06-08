class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(len(grid)):
            n=len(grid[i])
            for j in grid[i]:
                if j>=0:
                    n-=1
                else:
                    break
            ans+=n
        return ans      
