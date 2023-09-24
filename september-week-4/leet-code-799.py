class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        prev_glass=[poured]
        for row in range(1,query_row+1):
            curr=[0]*(row+1)
            for i in range(row):
                left_over=prev_glass[i]-1
                if left_over>0:
                    curr[i]+=(0.5*left_over)
                    curr[i+1]+=(0.5*left_over)
            prev_glass=curr
        return min(1,prev_glass[query_glass]) 
