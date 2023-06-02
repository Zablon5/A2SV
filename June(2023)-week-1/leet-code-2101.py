class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj=defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i+1,len(bombs)):
                x1,y1,r1=bombs[i]
                x2,y2,r2=bombs[j]
                d=sqrt((x1-x2)**2 + (y1-y2)**2)
                if d<=r1:
                    adj[i].append(j)
                if d<=r2:
                    adj[j].append(i)
        def bfs(i):
            q=deque([i]) 
            visited=set([i]) 
            while q:
                g=q.popleft()  
                for neighbour in adj[g]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        q.append(neighbour)   
            return len(visited)       
        ans=0
        for i in range(len(bombs)):
            ans=max(ans,bfs(i)) 
        return ans             
