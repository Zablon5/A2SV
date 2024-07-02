class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mp={}
        for i in nums1:
            if i not in mp:
                mp[i]=1
            else:
                mp[i]+=1   
        ans=[]         
        for i in nums2:
            if i in mp and mp[i]>0:
                ans.append(i)
                mp[i]-=1
        return ans