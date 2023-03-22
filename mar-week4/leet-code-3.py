class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count={}
        longest=0
        l=0
        for r in range(len(s)):
            count[s[r]]=1+count.get(s[r],0)
            while count[s[r]]>1:
                count[s[l]]=count[s[l]]-1
                l=l+1
            longest=max(longest,r-l+1)
        return longest        
        
