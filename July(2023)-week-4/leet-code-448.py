class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n=len(nums)
        nm=set(nums)
        ans=[]
        for i in range(1,n+1):
            if i not in nm:
                ans.append(i)
        return ans 
