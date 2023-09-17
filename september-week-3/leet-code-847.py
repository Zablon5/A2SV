class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n=len(graph)
        mask=[1<<i for i in range(n)]
        visited=(1<<n)-1
        q=deque([(i,mask[i]) for i in range(n)])
        steps=0
        visitedstate=[{mask[i]} for i in range(n)]
        while q:
            count=len(q)
            while count:
                curr,visit=q.popleft()
                if visit==visited:
                    return steps
                for neigh in graph[curr]:
                    newvisit=visit|mask[neigh]    
                    if newvisit==visited:
                        return steps+1
                    if newvisit not in visitedstate[neigh]:
                        visitedstate[neigh].add(newvisit)
                        q.append((neigh,newvisit))
                count-=1
            steps+=1
        return inf                
        
