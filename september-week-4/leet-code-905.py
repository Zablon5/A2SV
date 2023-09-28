class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in nums:
            if not i%2:
                even.append(i)
            else:
                odd.append(i)
        return even+odd
