from collections import defaultdict,deque
def dfs():

    n,m=map(int,input().split())
    a,b=map(int,input().split())
    queue=deque([a])
    track={a:-1}
    graph=defaultdict(list)
    for _ in range(m):
        u,v=map(int,input().split())
        graph[u].append(v)
        graph[v].append(u)
    while queue:
        node=queue.popleft()   
        if node==b:
            break
        for neighbour in graph[node]:
            if neighbour not in track:
                track[neighbour]=node
                queue.append(neighbour)
    if b not in track:
        print(-1)
        return     
    ans=[]
    curr=b
    while curr!=-1:
        ans.append(curr)
        curr=track[curr] 
    print(len(ans)-1)    
    print(*ans[::-1])           
dfs()
