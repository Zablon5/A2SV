class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        def isvalid(threshold):
            i,cnt=0,0
            while i<len(nums)-1:
                if (nums[i+1]-nums[i])<=threshold:
                    cnt+=1
                    i+=2
                else:
                    i+=1
                if cnt==p:
                    return True
            return False
        if p==0:
            return 0  
        nums.sort()      
        l,r=0,10**9
        ans=10**9
        while l<=r:
            m=(l+r)//2
            if isvalid(m):
                ans=m
                r=m-1
            else:
                l=m+1
        return ans      
