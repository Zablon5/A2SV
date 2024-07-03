class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums = sorted(nums)
        if len(nums) <= 4:
            return 0
        w = nums[-4]-nums[0]    
        x = nums[-1]-nums[3]  
        y = nums[-2]-nums[2]
        z = nums[-3]-nums[1]
        return min(w, x, y, z) 
        