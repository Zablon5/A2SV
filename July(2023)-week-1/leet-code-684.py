class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n=len(edges)
        par={i:i for i in range(1,n+1)}
        rank=[1]*(n+1)
        def find(res):
            ver=res
            while par[ver]!=ver:
                par[ver]=par[par[ver]]
                ver=par[ver]
            return ver    
                
     
       
        def union(e1,e2):
            pe1=e1
            pe2=e2  
            
            if pe1!=pe2:
                if rank[pe1]>rank[pe2]:
                    par[pe2]=pe1
                    rank[pe1]+=rank[pe2]
                else:
                    par[pe1]=pe2
                    rank[pe1]+=rank[pe2] 
                   
            else:           
                return True
            
        for e1,e2 in edges:
            par1=find(e1)
            par2=find(e2)
            if par1 ==par2:
            
                return [e1,e2]
            else:    
                union(par1,par2) 
