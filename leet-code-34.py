class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        up=-1
        n=len(nums)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                up=mid
                l=mid+1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        low=-1
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]==target:
                low=mid
                r=mid-1
            elif nums[mid]>target:
                r=mid-1
            else:
                l=mid+1
        return [low,up]        
        
