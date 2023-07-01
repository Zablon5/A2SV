class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        ans=[]
        visited=set()
        g=defaultdict(list)
        for [u,v] in adjacentPairs:
            g[u].append(v)
            g[v].append(u)
        see=[]    
        for i in g:
            if len(g[i])==1:
                see.append(i)
            if len(see)==2:
                break
        start,end=see[0],see[1]  
        def dfs(x):
            ans.append(x)
            visited.add(x)
            for y in g[x]:
                if y not in visited:
                    dfs(y)
        dfs(start)     
        return ans  
