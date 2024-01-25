class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def rec(ind1,ind2,dp,ans):
            if (ind1,ind2) in dp:
                return dp[(ind1,ind2)]
            if ind1<0 or ind2<0:
                return 0
          
            match=0
            not_match=0
            if text1[ind1]==text2[ind2]:
                ans.append(text1[ind1])
                match=1+rec(ind1-1,ind2-1,dp,ans) 
            else:       
                not_match=max(rec(ind1-1,ind2,dp,ans),rec(ind1,ind2-1,dp,ans))
            dp[(ind1,ind2)]=match+not_match
            return match+not_match
        dp={}
        ans=[]
        an=rec(len(text1)-1,len(text2)-1,dp,ans)
       
        return an 
        