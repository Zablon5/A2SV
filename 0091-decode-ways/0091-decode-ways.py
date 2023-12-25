class Solution:
    
    def numDecodings(self, s):
        memo = [-1] * len(s)

        def helper(index):
            if index == len(s):
                return 1

            if s[index] == '0':
                return 0

            if memo[index] != -1:
                return memo[index]

            ways = helper(index + 1)

            if index < len(s) - 1 and int(s[index:index + 2]) <= 26:
                ways += helper(index + 2)

            memo[index] = ways
            return ways

        return helper(0)

        
        