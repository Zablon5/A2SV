n=int(input())
mat=[[0 for i in range(n)] for j in range(n)]
inp=[]
for i in range(n):
    adj=list(map(int,input().split()))
    inp.append(adj)
for i in range(n):
    for j in range(inp[i][0]):
        mat[i][inp[i][j+1]-1]=1
    print(*mat[i])
