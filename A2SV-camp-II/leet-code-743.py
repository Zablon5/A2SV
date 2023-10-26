class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        g=defaultdict(list)
        for u,v,t in times:
            g[u].append([v,t])
        
        tms={node: float('inf') for node in range(1,n+1)}   
        tms[k]=0
   
        heap=[(0,k)]
        visited=set()

        while heap:
            curr_time,curr_node=heappop(heap)
            if curr_node in visited:
                continue
             
            visited.add(curr_node)    
            for node,t in g[curr_node]:
                ttime=curr_time+t
               
            
                if ttime<tms[node]:
                    tms[node]=ttime
                        
                    heappush(heap,(ttime,node))
       
        return max(tms.values()) if len(visited)==n else -1  
