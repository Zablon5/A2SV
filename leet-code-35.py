class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        ind=len(nums)
        while l<=r:
            mid=(l+r)//2
            if nums[mid]>=target:
                ind=mid
                r=mid-1
            else:
                l=mid+1
        return ind           
