class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        def rec(coins,amount,i,dp):
            if amount==0:
                return 1
            if i>=len(coins) or amount<0:
                return 0
            if (i,amount) in dp:
                return dp[(i,amount)]    
            pick=rec(coins,amount-coins[i],i,dp)    
            not_pick=rec(coins,amount,i+1,dp)
            count=pick+not_pick
            dp[(i,amount)]=count
            return count
        dp={}
        return rec(coins,amount,0,dp)   
