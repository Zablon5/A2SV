class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        lis=[]
        def helper(i,lis):
            if i==len(nums):
                lis=lis.copy()
                ans.append(lis)
                return
               
            lis.append(nums[i])
            helper(i+1,lis)
            lis.pop()
            helper(i+1,lis)
        helper(0,lis)
        return ans
         
