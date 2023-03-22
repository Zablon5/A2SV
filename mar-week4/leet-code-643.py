class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        cu=sum(nums[:k])
        mx=cu/k
        l=0
        for r in range(k,len(nums)):
            cu=cu-nums[l]+nums[r]
            mx=max(mx,cu/k)
            l+=1
        return mx   
