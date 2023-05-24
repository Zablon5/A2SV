class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph=defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited=set()    
        queue=deque([source])
        while queue:
            node=queue.popleft()
            if node==destination:
                    return True
                
            for neighbour in graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
        return False         
