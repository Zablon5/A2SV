class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runnin=[0]*len(nums)
        runnin[0]=nums[0]
        for i in range(1,len(nums)):
            runnin[i]=runnin[i-1]+nums[i]
        return (runnin)
