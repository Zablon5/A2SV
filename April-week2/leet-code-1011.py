class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l=max(weights)
        r=sum(weights)
        while l<r:
            mid=(l+r)//2
            best=1
            s=0
            for i in weights:
                s+=i
                if s>mid:
                    best+=1
                    s=i

            if best<=days:
                r=mid
            else:
                l=mid+1
        return l            
