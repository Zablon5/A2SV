class Solution:
    def reverse(self, x: int) -> int:
        sig=1
        ans=[]
        if x<0:
            x=x*-1
            sig=-1
        while x>9:
            i=x%10
            ans.append(str(i))
            x=x//10
        ans.append(str(x))    
        ans=(int("".join(ans)))   
        if -2**31<=sig*ans<= 2**31-1:
            return sig*ans
        else:
            return 0    
