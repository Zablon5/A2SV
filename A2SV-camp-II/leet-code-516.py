class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        s2=s[::-1]
        def rec(ind1,ind2,dp):
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if ind1<0 or ind2<0:
                return 0
            match=0
            not_match=0    
            if s2[ind2]==s[ind1]:
                match=1+rec(ind1-1,ind2-1,dp)
            else:

                not_match=max(rec(ind1,ind2-1,dp),rec(ind1-1,ind2,dp)) 
            dp[(ind1,ind2)]=max(match,not_match)
            return max(match,not_match)    
        dp={}      
        return rec(len(s)-1,len(s)-1,dp)   
