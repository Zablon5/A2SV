n,m=list(map(int,input().split()))
ans=-1

if m%n==0:    
    ans=0
    d=m/n
    while(d%2==0):
            ans+=1
            d=d/2
    while(d%3==0):
            ans+=1
            d=d/3
    if d!=1:
            ans=-1
print(ans)     
