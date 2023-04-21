def solve():
    n=int(input())
    for _ in range(n):
        l=int(input())
        tree=input().split()
        p,v,d=[0] * (l+1), [0] * (l+1), [0] * (l+1)
        for i in range(1,l+1):
            p[i]=int(tree[i-1])
            d[i]+=1
            d[p[i]]+=1
        leaf=[]
        for i in range(1,l+1):
            if d[i]==1:
                leaf.append(i)
        if l==1:
            print("1")
            print("1")
            print("1")
            continue
        print(len(leaf))    
    
        for i in leaf:
            path=[]
            j=i
            while not v[j]:
                path.append(j)
                v[j]=1
                j=p[j]
            print(len(path))
            path.reverse()
            print(" ".join(str(i) for i in path)) 
solve()            
