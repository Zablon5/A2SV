class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0

        def is_odd(num):
            return num % 2

        for num in arr:
            
            if is_odd(num):
                count += 1
            else :
                count = 0
            if count == 3:
                return True
      
        return False