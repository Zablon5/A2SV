class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count=Counter(nums)
        res=0
        seen=set()
        for i in count:
            if i not in seen and k-i in count:
                if i==k-i:
                    res+=count[i]//2
                 
                else:
                    res += min(count[i],count[k-i])
                seen.add(i)
                seen.add(k-i)    
        return res
