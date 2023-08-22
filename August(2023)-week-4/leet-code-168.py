class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        
        ans=''
        while(columnNumber):
            x=(columnNumber-1)%26
            ans=chr(x+65)+ans
            columnNumber=(columnNumber-1)//26
        return ans
