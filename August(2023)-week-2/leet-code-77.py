class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        stack=[]
        res=[]
        stack.append(([],1))
        while stack:
            cur,curind=stack.pop()
            if len(cur)==k:
                res.append(cur)
            
            for i in range(curind,n+1):
                newc=cur+[i]
                stack.append((newc,i+1))
        return res    
