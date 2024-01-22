class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        count=Counter(nums)
        dup=0
        loss=0
        for i in range(1,n+1):
            if i not in count:
                loss=i
            if count[i]==2:
                dup=i
        return [dup,loss]
            
            
            
        