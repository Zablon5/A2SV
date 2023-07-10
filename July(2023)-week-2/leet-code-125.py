class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=[]
        for i in s:
            if 97<=ord(i)<=122 or 65<=ord(i)<=90:
                clean.append(i.lower())
            elif 48<=ord(i)<=57:
                clean.append(i) 
        l=0
        r=len(clean)-1
        while r>=l:
            if clean[l]!=clean[r]:
                return False
            else:
                l+=1
                r-=1    
        return True        

