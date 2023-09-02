class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dp={len(s):0}
        dicti=set(dictionary)
        def rec(i):
            
            if i in dp:
                return dp[i]    
            res=1+rec(i+1)
            for j in range(i,len(s)):
                if s[i:j+1] in dicti:
                    res=min(rec(j+1),res)
            dp[i]=res        
            return res
        return rec(0) 
