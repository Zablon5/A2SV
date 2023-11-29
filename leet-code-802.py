class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        path=[0 for _ in range(n)]
        visited=[0 for _ in range(n)]

        ans=[]

        def dfs(node):
            for child in graph[node]:
                if not visited[child]:
                    visited[child]=1
                    path[child]=1
                    if dfs(child):
                        return True
                    path[child]=0
                elif path[child]:
                    return True  
            return False        
        for i in range(n):
            if not visited[i]:
                visited[i]=1
                path[i]=1
                if not dfs(i):
                    ans.append(i) 
                    path[i]=0  
            elif not path[i]:
                ans.append(i)   
        return ans           
