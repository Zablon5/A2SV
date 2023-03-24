class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0 or x==1:
            return x
        l = 0
   
        r = x

        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x<(mid+1)*(mid+1):
                return mid
            elif mid * mid < x:
                l = mid + 1
            else:
                r = mid - 1
           
