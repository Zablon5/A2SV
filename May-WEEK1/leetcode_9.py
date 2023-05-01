class Solution:
    def isPalindrome(self, x: int) -> bool:
        l=0
        sx=str(x)
        r=len(sx)-1
        while l<r:
            if sx[l]!=sx[r]:
                return False
            l+=1
            r-=1
        return True        
