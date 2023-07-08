class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n=len(s)
        par={i:i for i in range(n)}
        rank=[1]*n

        def find(x):
            res=x
            while par[res]!=res:
                par[res]=par[par[res]]
                res=par[res]
            return res
        def union(x,y):
            parx=find(x)
            pary=find(y)
            if parx!=pary:
                if rank[parx]>rank[pary]:
                    par[pary]=parx
                    rank[parx]+=rank[pary]
                else:
                    par[parx]=pary
                    rank[pary]+=rank[parx]
        for x,y in pairs:
            union(x,y)   
        m=defaultdict(list)    
        
        res=[]      
        for i in range(n):
            m[find(i)].append(s[i])
        print(m)    
        for i in m.keys():
            m[i].sort(reverse=True)    
        for i in range(n):
            res.append(m[find(i)].pop())
        return ''.join(res)   
