class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        def inverter(y):
            inverted = 0
            while y:
                inverted = inverted*10 + y%10
                y = y//10
            return inverted
        return inverter(x) == x
            
        