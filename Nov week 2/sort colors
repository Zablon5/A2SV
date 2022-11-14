class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minind=i
            for j in range(i+1,len(nums)):
                if nums[minind]>nums[j]:
                    minind=j
            nums[minind],nums[i]=nums[i],nums[minind] 
