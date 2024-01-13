class Solution:
    def minSteps(self, s: str, t: str) -> int:
        mps,mpt,ans=Counter(s),Counter(t),0
        for c in mpt:
            if c not in mps:
               
                ans+=mpt[c]
            elif mpt[c]>mps[c]:
                ans+=abs(mpt[c]-mps[c])
      
        return ans
        