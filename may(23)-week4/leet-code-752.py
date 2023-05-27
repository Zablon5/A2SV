class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1
       
        q=deque()
        q.append(["0000",0])
        visited=set(deadends)
       
                
        while q:
            key,count=q.popleft()
            if key==target:
                return count
            res=[]
            for i in range(4):
                digit=str((int(key[i])+1)%10)
                res.append(key[:i]+ digit + key[i+1:])
                digit=str((int(key[i])-1+10)%10)
                res.append(key[:i]+digit + key[i+1:])    
            for child in res:
               
                if child not in visited:
                    
                    q.append([child,count+1])
                    visited.add(child)
        return -1  
