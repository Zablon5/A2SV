import re
class Solution:
    def sortSentence(self, s: str) -> str:
        x=s.split()
        word={}
        ans=''
        for i in x:
            word[i[-1]]=i[:-1]
        for i in sorted(word):
            ans=ans+''.join(word[i])+' '
        ans=ans[:-1]    
        
        return ans 