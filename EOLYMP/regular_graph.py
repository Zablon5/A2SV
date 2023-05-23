from collections import defaultdict
def check():

    graph=defaultdict(list)
    v,e=list(map(int,input().split()))
  
       
    for _ in range(e):
        ed=list(map(int,input().split()))
            
        graph[ed[0]].append(ed[1])
        graph[ed[1]].append(ed[0])
       
    ans=len(graph[1]) 
    babs=True    
    for i in range(v):
        if ans!=len(graph[i+1]):
            return False
        else:
            continue    
    return babs
               
if check():
    print('YES')
else:
    print('NO')
