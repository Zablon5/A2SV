class Solution:
    def minDeletions(self, s: str) -> int:
        counter=Counter(s)
        lst=list(counter.values())
        lst.sort() 
        ln=len(lst)
        ans,l,r=0,ln-2,ln-1
        while l>=0:
            diff=(lst[l]-lst[r]+1)
            if lst[l]>=lst[r]:
                if (lst[l]-diff)>0:
                    ans+=diff
                    lst[l]-=diff
                else:
                    ans+=lst[l]
                    lst[l]=0
            l-=1
            r-=1
        
        return ans 
