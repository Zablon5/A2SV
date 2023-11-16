class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(ind1,ind2,dp):
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if ind1<0 or ind2<0:
                return 0
          
            match=0
            not_match=0
            if text1[ind1]==text2[ind2]:

                match=1+rec(ind1-1,ind2-1,dp) 
            else:       
                not_match=max(rec(ind1-1,ind2,dp),rec(ind1,ind2-1,dp))
            dp[(ind1,ind2)]=match+not_match
            return match+not_match
        dp={}
        return rec(len(text1)-1,len(text2)-1,dp)    
        
