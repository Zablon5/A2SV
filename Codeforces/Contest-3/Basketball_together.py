import math
n,D=map(int,input().split())
p=list(map(int,input().split()))
p=sorted(p,reverse=True)
w=0
s=0
ans=[]
for i,val in enumerate(p):
    ans.append(math.ceil((D+1)/val))
for i in ans:
    s+=i
    if s<=n:
        w=w+1
print(w) 
