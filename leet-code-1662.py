class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return ''.join(i for i in word1)==''.join(i for i in word2)
        
