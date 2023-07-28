class Solution:
    def rob(self, nums: List[int]) -> int:
   
        h1=0
        h2=0
        for m in nums:
            res=max(h1+m,h2)
            h1=h2
            h2=res
        return h2    
