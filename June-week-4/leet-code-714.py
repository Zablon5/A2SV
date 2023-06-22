class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n=len(prices)
        h,f=[0]*n,[0]*n

        h[0]=-prices[0]
        for i in range(1,n):
            h[i]=max(h[i-1],f[i-1]-prices[i])
            f[i]=max(f[i-1],h[i-1]+prices[i]-fee)
        return f[-1]     
