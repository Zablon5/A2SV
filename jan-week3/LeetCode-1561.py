class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        spile=sorted(piles,reverse=True)
        le=len(spile)
        result=0
        

        for i in range(int(le/3)):
            result+=spile[2*i+1]
        return result    
