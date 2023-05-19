from collections import defaultdict

graph=defaultdict(list)

def addEdge(u,v) :
    graph[u].append(v)  
       

   
n=input()
t=int(input())
for _ in range(t):
    v=list(map(int,input().split()))
    if len(v)==3:
        addEdge(v[1],v[2])
        addEdge(v[2],v[1])
    else:
        print(*graph[v[1]])
