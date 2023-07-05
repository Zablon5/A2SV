class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp=defaultdict(list)
        n=len(nums)
        for i in range(n):
            mp[nums[i]].append(i)
        for i in mp:
            if len(mp[i])>1:
                l=0
                r=1
                while r<len(mp[i]):
                    if abs(mp[i][l]-mp[i][r])>k:
                        l+=1
                        r+=1
                        
                    else:
                        return True   
        return False                 
