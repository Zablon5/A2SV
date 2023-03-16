class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        def pow(x,y):
            mod=10**9+7
            if y==0:
                return 1
            ans=pow(x,y//2)
            ans=(ans*ans)%mod
            if (y%2):
                ans=(ans*x)%(mod)
            return ans
        odd=n//2        
        even=n//2 + n%2
        return (pow(5,even)*pow(4,odd))%mod
