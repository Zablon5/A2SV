class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(x):
            ans=''
            x=str(x)
            for i in range(len(x)):
                ans=x[i]+ans
            return int(ans)   
        mp={}
        count=0
        for i in range(len(nums)):
            if nums[i]-rev(nums[i]) in mp:
                mp[nums[i]-rev(nums[i])]+=1
               
            else:
                mp[nums[i]-rev(nums[i])]=1
        for i in mp:
            count+=comb(mp[i],2) 
       
        return count%(10**9+7)    
