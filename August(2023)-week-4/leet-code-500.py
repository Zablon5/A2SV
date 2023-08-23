class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        s1=set("qwertyuiop")
        s2=set("asdfghjkl")
        s3=set("zxcvbnm")
        ans=[]
        for w in words:
            t1=0
            t2=0
            t3=0
            for i in w.lower():
                if i not in s1:
                    t1=0
                    break
                else:
                    t1=1    
            for i in w.lower():
                if i not in s2:
                    t2=0
                    break
                else:
                    t2=1    
            for i in w.lower():
                if i not in s3:
                    t3=0

                    break 
                else:
                    t3=1
            if t1 or t2 or t3:
                ans.append(w)
        return ans 
