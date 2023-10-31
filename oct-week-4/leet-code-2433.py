class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans=[pref[0]]
        temp=pref[0]
        for i in range(1,len(pref)):
            val=temp^pref[i]
            ans.append(val)
            temp^=val
        return ans     
        
