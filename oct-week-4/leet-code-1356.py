class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda val:(bin(val).count('1'),val))
        return arr
