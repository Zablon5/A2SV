from collections import defaultdict
import heapq
n,m=list(map(int,input().split()))
roads=defaultdict(list)
railways=defaultdict(list)
for _ in range(m):
    u,v=list(map(int,input().split()))
    railways[u].append(v)
    railways[v].append(u)
for i in range(1,n+1):
    roads[i]=[j for j in range(1,n+1) if j not in railways[i] and j!=i]
def shortest(grpah,n):
    distances=[float("inf")]*(n+1)
    heap=[(0,1)]
    distances[1]=0
    while heap:
        dist,node=heapq.heappop(heap)
        for new_node in grpah[node]:
            if dist+1 < distances[new_node]:
                distances[new_node]=dist+1
                heapq.heappush(heap,(dist+1,new_node))

    return distances[n]  
ans=max(shortest(roads,n),shortest(railways,n))
if ans==float('inf'):
    print(-1)
else:
    print(ans)  
