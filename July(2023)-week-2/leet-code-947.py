class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n=len(stones)
        par={i:i for i in range(n)}
        rank=[1]*n
        def find(st):
            while par[st]!=st:
                par[st]=par[par[st]]
                st=par[st]
            return st
        def union(st1,st2):
            
            parst1=find(st1)
            parst2=find(st2)        
            if parst1!=parst2 :
                if rank[st1]>rank[st2]:
                    par[parst2]=parst1
                    rank[parst1]+=rank[parst2]
                    rank[parst2]=0
                else:
                    par[parst1]=parst2
                    rank[parst2]+=rank[parst1]   
                    rank[parst1]=0 
        for i in range(n):
            row1,col1=stones[i]
            for j in range(i+1,n):
                row2,col2=stones[j]
                if row1==row2 or col1==col2:
                    union(i,j)

        for i in rank:
            if i!=0:
                n-=1
        return n
