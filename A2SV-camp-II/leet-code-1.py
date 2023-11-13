class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup={}
        for i,val in enumerate(nums):
            x=target-val
            if x in lookup:
                return [i,lookup.get(x)]
            else:
                lookup[val]=i    
