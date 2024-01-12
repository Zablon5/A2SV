class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i,j,first,second=0,len(s)-1,0,0
        
        lookup=('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        
        while i<j:
            if s[i] in lookup:
                first+=1
            if s[j] in lookup:
                second+=1
            i+=1
            j-=1
                
            
        return first==second
        