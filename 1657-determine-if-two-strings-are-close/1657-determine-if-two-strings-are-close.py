class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        same=True
    
        count1,count2 = [i for i in Counter(word1).values()],[j for j in Counter(word2).values()]
        for c in set(word1):
            if c not in set(word2):
                same=False
                break
        sameList=True
        if len(count1)!=len(count2):
            return False
        for i in count1:
            if countOf(count1,i)!=countOf(count2,i):
                sameList=False
                break
      
        return same and sameList
        