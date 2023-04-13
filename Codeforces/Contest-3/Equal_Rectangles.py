q=int(input())
for _ in range(q):
    
    n=int(input())
    s=list(map(int,input().split()))
    s.sort()
   
    area=s[0]*s[-1]
    
    ans='YES'
    for i in range(n):
        l=i*2
        r=4*n-(i*2)-1
        if area!=s[l]*s[r] or s[l]!=s[l+1] or s[r]!=s[r-1]:
            ans='NO'
            
        
          
    print(ans)      
