class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        count=0
        while a or b or c:
            if c&1:
                if a&1==0 and b&1==0:
                    count+=1
            else:
                count+=(a&1) + (b&1)
            a=a>>1
            b=b>>1
            c=c>>1
        return count  
