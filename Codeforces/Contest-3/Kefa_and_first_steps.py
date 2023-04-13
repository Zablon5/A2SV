n=int(input())
a=list(map(int,input().split()))

i=0
j=1

c_max=1
count=1
while j<n:
    
    if a[j]>=a[i]:
        count+=1
        j+=1
        i+=1
        c_max=max(c_max,count)
    else:
        
        count=1
        j+=1
        i+=1
print(c_max)   
