class Solution:
    def findValueOfPartition(self, nums: List[int]) -> int:
        nums.sort()
        
        ans = float('inf')
        n = len(nums)
        for i in range(1,n):
            ans = min(ans, abs(nums[i] - nums[i-1]))
        return ans