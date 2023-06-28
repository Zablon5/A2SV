class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        g=defaultdict(list)
        for i,(u,v) in enumerate(edges):
            g[u].append([v,succProb[i]])
            g[v].append([u,succProb[i]])
        mp=[0]*n
        mp[start]=1
        q=deque([start])    
        while q:
            curr=q.popleft()
            for next,prob in g[curr]:
                if mp[curr]*prob>mp[next]:
                    mp[next]=mp[curr]*prob
                    q.append(next)
        return mp[end]   
