class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[0]*len(temperatures)
        stack=[]
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0]<v:
                st,si=stack.pop()

                ans[si]=i-si
            stack.append([v,i])  
        return ans
