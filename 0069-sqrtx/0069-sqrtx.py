class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l=1
        r=x
        ans=1
        while l<=r:
            mid=(l+r)//2
            if mid*mid<=x:
                ans=mid
                l=mid+1

            elif mid*mid>x:
                r=mid-1
        return ans

        
