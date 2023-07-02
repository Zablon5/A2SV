class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        for u,v in prerequisites:
            g[u].append(v)
        visited=set()    
        def dfs(u):
            if g[u]==[]:
                return True
            if u in visited:
                return False
            visited.add(u)    
            for v in g[u]:
                if not dfs(v):
                    return False
            visited.remove(u)
            g[u]=[]
            return True
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
