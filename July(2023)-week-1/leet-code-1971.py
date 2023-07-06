class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
      
        rank=[1]*n
        parent={i:i for i in range(n)}
        def find(ver):
            res=ver
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res
        def union(e1,e2):
            pare1=find(e1) 
            pare2=find(e2)  
            if pare1!=pare2:
                if rank[pare1]>rank[pare2]:
                    parent[pare2]=pare1
                    rank[pare1]+=rank[pare2]
                else:
                    parent[pare1]=pare2
                    rank[pare2]+=rank[pare1]
               
        for u,v in edges:
            
            union(u,v)       
        return find(source)==find(destination)    
