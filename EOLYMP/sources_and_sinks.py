n=int(input())
mat=[]
for i in range(n):
    row=[]
    for j in list(map(int,input().split())):
        row.append(j)
    mat.append(row)    
source=set()
sink=set()
for i in range(n):
    
    for j in range(n):
        if mat[i][j]:
            
            source.add(i+1)
            
            sink.add(j+1)    
s=[]
si=[]
for i in range(1,n+1):
    if i in source:
        if i not in sink:
            s.append(i)
    elif i in sink:
        if i not in source:
            si.append(i)  
    else:
        s.append(i)
        si.append(i)    
print(len(s),end=' ')   
print(*s)
print(len(si),end=' ')   
print(*si)
