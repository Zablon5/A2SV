class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        h=0
        cur=0
        for i in gain:
            h=max(h,cur+i)
            cur+=i
        return h    
