class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        q=[0]*len(queries)
        w=[0]*len(words)
        ans=[0]*len(queries)
        for i in range(len(queries)):
            qw=queries[i]
            sm=123
            for l in qw:
                
                sm=min(sm,ord(l))
            q[i]=qw.count(chr(sm))  
        for i in range(len(words)):
            ww=words[i]
            smw=123
            for l in ww:
                
                smw=min(smw,ord(l))
            w[i]=ww.count(chr(smw)) 
        for i in range(len(q)):
            c=0
            for j in w:
                if q[i]<j:
                    c+=1
            ans[i]=c              
        return ans
