class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n=len(nums)
        ans=[]
        i=0
        while i<n:
            start=nums[i]
            while i+1 < n and nums[i+1]-nums[i] == 1:
                i += 1
            if start!=nums[i]:
                ans.append(str(start) + "->" + str(nums[i]))
            else: 
                ans.append(str(nums[i]))
            i += 1
        return ans   
