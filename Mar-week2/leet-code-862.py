class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        presum=[0]*(n+1)
        for i in range(1,n+1):
            presum[i]=presum[i-1]+nums[i-1] 
        deq=[]
        res=n+1
        for i in range(n+1):
            while deq and presum[i]-presum[deq[0]]>=k:
                res=min(res,i-deq.pop(0))
            while deq and presum[i]<=presum[deq[-1]]:
                deq.pop()
            deq.append(i)
        return res if res<=n else -1                   
