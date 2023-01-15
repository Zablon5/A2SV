class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        lisints=list(map(int,nums))
        X=sorted(lisints,reverse=True)
        
        ans=str(X[k-1])
        return ans
        
