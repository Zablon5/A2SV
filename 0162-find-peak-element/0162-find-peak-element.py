class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0    
        l,m,r=0,1,2
        while r<len(nums):
            if nums[l]<nums[m]>nums[r]:
                return m
            l+=1
            m+=1
            r+=1    
        if nums[0]>nums[1]:
            return 0
        if nums[len(nums)-1]>nums[len(nums)-2]:
            return len(nums)-1    
        