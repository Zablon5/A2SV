class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res=set()
        lookup=set()
        for i in range(len(s)-9):
            x=s[i:i+10]
            if x in lookup:
                res.add(x)
            lookup.add(x) 
        return list(res)    

               
