class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        p_counter,s_counter={},{}
        l=0
        for i in range(len(p)):
            p_counter[p[i]]=1+p_counter.get(p[i],0)
            s_counter[s[i]]=1+s_counter.get(s[i],0)
        ans=[0] if p_counter==s_counter else []
        for r in range(len(p),len(s)):
            s_counter[s[r]]=1+s_counter.get(s[r],0)
            s_counter[s[l]]=-1+s_counter.get(s[l],0)
            if s_counter[s[l]]==0:
                s_counter.pop(s[l])
            l+=1 
            if s_counter==p_counter:
                ans.append(l) 
        return ans         
