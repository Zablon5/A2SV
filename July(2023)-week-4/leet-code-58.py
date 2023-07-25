class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ns=list(s.split())  
        return len(ns[-1])
