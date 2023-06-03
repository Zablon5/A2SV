class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        g=defaultdict(list)
        for i in range(n):
            g[manager[i]].append(i)
        q=deque([(headID,0)])    
        ans=0
        while q:
            id,time=q.popleft()
            ans=max(time,ans)
            for emp in g[id]:
                q.append([emp,time+informTime[id]])
        return ans    
