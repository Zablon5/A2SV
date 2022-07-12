class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        a=[0]*len(nums)
        for i in range(len(nums)):
            n=0

            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    n=n+1
                    a[i]=n

        return a