l=int(input())
stack=[1]
ans=0
for _ in range(l):
    line=input().split()
    if line[0]=='add':
        ans+=stack[-1]
    elif line[0]=='end':
        stack.pop()
    else:
        stack.append(min(2**32,int(line[1])*stack[-1]))
if ans>2**32-1:
    print("OVERFLOW!!!")
else:
    print(ans)
