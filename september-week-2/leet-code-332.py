class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph=defaultdict(list)
        for edge in tickets:
            v1,v2=edge[0],edge[1]
            graph[v1].append(v2)
        for p in graph:
            graph[p].sort()    
        
        res=['JFK']
        def dfs(vertex):
            if len(res)==len(tickets)+1:
                return True
            if vertex not in graph:
                return False
            temp=graph[vertex]     
            for i,v in enumerate(temp):
                graph[vertex].pop(i)
                res.append(v)
                if dfs(v):return True
                graph[vertex].insert(i,v)
                res.pop()
               
        dfs('JFK')        
        return res
