class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)
        def rec(i,cur):
            if i==n:
                if cur not in ans:
                    ans.append(cur.copy())  
                return
            cur.append(nums[i])   
            rec(i+1,cur)
            cur.pop()
            rec(i+1,cur)
        rec(0,[])
        return ans           
