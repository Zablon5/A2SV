class Solution:
    def totalMoney(self, n: int) -> int:
        i=1
        ans=0
        mark=0
        for j in range(n):
            if i==8:
                mark+=1
                i=1
            ans+=i+mark
            i+=1
        return ans
