class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans=0
        nod=[]
        for i in bank:
            cnt=i.count('1')
            if cnt>0:
                
                nod.append(cnt)
        i,j=0,1
        while j<len(nod):
            ans+=(nod[i]*nod[j])
            i+=1
            j+=1
        return ans
        