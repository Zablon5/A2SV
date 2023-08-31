class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        ac=''
        for word in words:
            ac+=word[0]
        return ac==s    
