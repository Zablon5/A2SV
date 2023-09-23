class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        def is_pre(w1,w2):
            if len(w1)+1!=len(w2): return False
            i=0
            for j in w2:
                if i<=len(w1)-1:
                    if w1[i]==j:
                        i+=1
            return i==len(w1)       

        words.sort(key=len)    
        n=len(words)
        dp=[1]*n
        ans=1
        for i in range(1,n):
            for j in range(i):
                if is_pre(words[j],words[i]) and dp[i]<dp[j]+1:
                    dp[i]=dp[j]+1
            ans=max(ans,dp[i])        
        return ans    
