class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ms={}
        for l in s:
            ms[l]=ms.get(l,0)+1
        for l in t:
            if l not in ms or ms[l]==0:
                return l
            else:
                ms[l]-=1
