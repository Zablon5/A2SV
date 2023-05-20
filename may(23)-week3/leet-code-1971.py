class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=set()    
        def dfs(node,visited):
            visited.add(node)
            if node==destination:
                return True
            for Node in graph[node]:
                if Node not in visited and dfs(Node,visited):
                    return True
            return False
        return dfs(source,visited)            
         
