n=int(input())
mat=[]
for _ in range(n):
    row=list(map(int,input().split()))
    mat.append(row)
visited=set()    

for i in range(n):
    ans=[]
    for j in range(n):
        if mat[i][j]:
            ans.append(j+1)
            
    print(len(ans),end=' ')         
    print(*ans)
