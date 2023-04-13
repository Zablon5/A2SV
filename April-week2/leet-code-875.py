class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        while l<=r:
            mid=(l+r)//2
            hr=0
            for i in piles:
                if i%mid==0:
                    hr+=i/mid
                else:
                    hr+=i//mid + 1
            if hr<=h:
                r=mid-1
     
            else:
                l=mid+1
        return l           
