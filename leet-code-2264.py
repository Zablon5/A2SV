class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans=''
        n=len(num)
        l, r=0,3
        while r<=n:
            if num[l:r]=='000' and ans=='':
                ans=num[l:r]
                

            elif int(num[l]) and int(num[l:r])/int(num[l])==111:
                if ans=='':
                    ans=num[l:r]
                else:
                    ans=str(max(int(ans),int(num[l:r])))
            r+=1
            l+=1
        return ans
