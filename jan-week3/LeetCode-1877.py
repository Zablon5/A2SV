class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        sum=[]
        num=sorted(nums)
        le=len(nums)
        for i in range(le):
            if i<=le/2-1:
                sum.append(num[i]+num[le-1-i])
        return max(sum)    
