from collections import defaultdict

n=int(input())
mat=[]
for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
visited=set()    
count=0
for i in range(n):
    for j in range(n):
        if ((i,j) and (j,i) )not in visited and mat[i][j]:
            count+=1
            visited.add((i,j))
print(count)
