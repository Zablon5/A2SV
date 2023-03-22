class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        s_count={}
        l=0
        mx=0
        for r in range(len(s)):
            s_count[s[r]]=1+s_count.get(s[r],0)
            while (r-l+1)-max(s_count.values())>k:
                s_count[s[l]]=-1+s_count[s[l]]
                l+=1
            mx=max(mx,r-l+1)    
        return mx 
