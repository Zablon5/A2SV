class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
       
        fstr=s1+s2+baseStr
        pars1={(i):(i) for i in fstr}
        def find(l):
            ans=(l)
            while pars1[ans]!=ans:
                pars1[ans]=pars1[pars1[ans]]
                ans=pars1[ans]
            return ans
        def union(l1,l2):
            parl1=find(l1) 
            parl2=find(l2) 
            if parl1!=parl2:
                if ord(parl1)<ord(parl2):
                    pars1[parl2]=parl1
                else:
                    pars1[parl1]=parl2    
        for i in range(len(s1)):
            union(s1[i],s2[i])
        ans=[]    
        for i in baseStr:
            p=find(i) 
            ans.append(p)    
        return "".join(ans)           
