class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        for i in range(n):
            if i%2==0:
                ans+=nums[i]
        return ans      
