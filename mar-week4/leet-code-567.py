class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count=Counter(s1)
        s2_count=Counter(s2[:len(s1)])
        l=0
        if s1_count==s2_count:
            return True
        for r in range(len(s1),len(s2)):
            s2_count[s2[r]]=s2_count.get(s2[r],0)+1
            s2_count[s2[l]] = s2_count[s2[l]] - 1
            
            if s2_count[s2[l]]==0:
                s2_count.pop(s2[l])
            l+=1    
            if s2_count==s1_count:
                return True
        return False        
