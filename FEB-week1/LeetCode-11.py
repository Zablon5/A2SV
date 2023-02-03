class Solution:
    def maxArea(self, height: List[int]) -> int:
        h=height
        ans=0
        l,r=0,len(h)-1
        while l<r:
            ans=max(ans,min(h[l],h[r])*(r-l))
            if h[r]>h[l]:
                l+=1
            else:
                r-=1
        return ans            
