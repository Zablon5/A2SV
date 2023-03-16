class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            x=1/x
            n=-n
        if n==0:
            return 1
        if n==1:
            return x
        if n==2:
            return x*x
        if n==3:
            return x*x*x
        if n>3:
            if n%2==0:
                return (self.myPow(x,n//2))**2
            else:
                return x*(self.myPow(x,n//2))**2
