class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        for i in range(len(nums1)):
            
            x=0
            for j in range(nums2.index(nums1[i])+1,len(nums2)):
                if nums1[i]<nums2[j] and x==0:
                    x=nums2[j]
            if x!=0:
                ans.append(x)
            else: ans.append(-1)
        return ans                
                       

                
