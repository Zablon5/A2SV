class Solution(object):
    def getSum(self, a, b):
        
        mask = 0xffffffff
        a = a & mask 
        while b:
            sum = (a^b) & mask
            carry = ((a&b)<<1) & mask
            a = sum
            b = carry

        if (a>>31) & 1:
            return ~(a^mask)
        return a
