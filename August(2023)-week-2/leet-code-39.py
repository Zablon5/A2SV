class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def backtrack(cur,i,total,n):
            if total==target:
                ans.append(cur[:])
                return
            if total>target or i>=n:
                return
            cur.append(candidates[i]) 
            backtrack(cur,i,total+candidates[i],n)
            cur.pop()
            backtrack(cur,i+1,total,n)  
        backtrack([],0,0,len(candidates))
        return ans 
