class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        q=[]
        maxsub=0
        
        
        for r in range(len(s)):

            if s[r] not in q:
                q.append(s[r])
                maxsub=max(maxsub,len(q))
            else:
                while s[r] in q:
                    q.pop(0)
                q.append(s[r])   
        return maxsub        
