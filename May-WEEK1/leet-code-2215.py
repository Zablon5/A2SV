class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        
        nums1=set(nums1)
        nums2=set(nums2)
        ans1=[]
        ans2=[]
        for i in nums1:
            if i not in nums2:
                ans1.append(i)
        for i in nums2:
            if i not in nums1:
                ans2.append(i)    
        return [ans1,ans2]            
