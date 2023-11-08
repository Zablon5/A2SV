class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

        mat=[[float('inf')] *n for _ in range(n)]

        for i in range(n):
            mat[i][i]=0
        for u,v,w in edges:
            mat[u][v]=mat[v][u]=w
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    mat[i][j]=min(mat[i][j],mat[i][via]+mat[via][j])

     
        cur=float('inf')
        ans=0
        for i in range(n):
            cnt=0
            for j in range(n):
                if 0<mat[i][j]<distanceThreshold+1:
                    cnt+=1
            
            if cnt<=cur:
                ans=i
                cur=cnt
       
        return ans
        
