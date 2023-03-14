class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=0
        r=len(s)-1
        def rev(l,r):
            if l>r:
                return
            else:
                s[l],s[r]=s[r],s[l]

                return rev(l+1,r-1)
        rev(l,r)


    
