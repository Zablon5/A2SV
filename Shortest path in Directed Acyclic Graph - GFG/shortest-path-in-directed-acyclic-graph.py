#User function Template for python3
from collections import defaultdict
from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        stack=[]
        adj=defaultdict(list)
        for u,v,w in edges:
            adj[u].append((v,w))
        visited=[0 for _ in range(n)]
        def dfs(node):
            for child,w in adj[node]:
                if not visited[child]:
                    visited[child]=1
                    dfs(child)
            stack.append(node)
           
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                dfs(i)
        dist=[float('inf') for _ in range(n)]
        dist[0]=0
        while stack:
            node=stack.pop()
            for child,w in adj[node]:
                if dist[node]+w<dist[child]:
                    
                    dist[child]=dist[node]+w
        for i in range(len(dist)):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist
                


#{ 
 # Driver Code Starts

#Initial Template for Python 3

from typing import List




class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends