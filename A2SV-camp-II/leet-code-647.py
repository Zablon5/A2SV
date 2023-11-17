class Solution:
    def countSubstrings(self, s: str) -> int:
        def isPalindrome(st):
            l=0
            r=len(st)-1
            while r>=l:
                if st[r]!=st[l]:
                    return False
                r-=1
                l+=1
            return True
        count=0    
        for i in range(len(s)):
            for j in range(i,len(s)):
                if isPalindrome(s[i:j+1]):
                    count+=1
        return count  
