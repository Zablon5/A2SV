class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def invert(s):
            ans=[]
            for i in s:
                if i=='1':
                    ans.append('0')
                else:
                    ans.append('1') 
                   
            return ''.join(ans)  
        def maker(n):

            s='0'
            for i in range(n-1):
                s=s+'1'+(invert(s))[::-1]
            
            return s    
        x=maker(n)

        return x[k-1]
