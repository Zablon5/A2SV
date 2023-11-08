from collections import defaultdict
import heapq
n, m = list(map(int,input().split()))
graph = defaultdict(list)
for _ in range(m):
    a,b,w = list(map(int,input().split()))
    graph[a].append([b,w])
    graph[b].append([a,w])
def dijkstra(graph,n):
    distances=[float('inf')]*(n+1)
    distances[1]=0
    heap=[(0,1,1)] #weight,node,pred_node
    pred={1:1}
    while heap:
        dist,node,pred_node = heapq.heappop(heap)
        for newnode,newdist in graph[node]:
            tot = newdist+dist
           
            if tot<distances[newnode]:
                distances[newnode]=tot
                heapq.heappush(heap,(tot,newnode,pred_node))
         
                pred[newnode]=node
    if distances[n]==float('inf'):
        print(-1)
    else:      
        ans=[n]     
        start=n
        while start!=pred[start]:
            ans.append(pred[start])
            start=pred[start]
        for i in ans[::-1]:
            print(i,end=' ')
dijkstra(graph,n)     
