class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        ans=0
        mark=0
        n=len(nums)
        for i in range(n):
            mark=0
            curr=[]
            for j in range(i,n):
                if nums[j]<=threshold:
                
                    if mark==0 and nums[j]%2==0:
                        curr.append(nums[j])
                        mark=1
                    elif mark==1 and nums[j]%2==1:
                        curr.append(nums[j])
                        mark=0
                    else:
                        
                        break
                else:
                    break
            ans=max(ans,len(curr)) 
        return ans 
