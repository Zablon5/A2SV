class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        i=len(nums)//3
        ans=[x for x in count if count[x]>i]
        return ans
