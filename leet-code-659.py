class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count=Counter(nums)
        last=defaultdict(int)
        n=len(nums)
        for num in nums:
            if not count[num]:
                continue
            count[num]-=1
            if last[num-1]:
                last[num-1]-=1
                last[num]+=1
            elif count.get(num+1) and count.get(num+2):
                count[num+1]-=1
                count[num+2]-=1
                last[num+2]+=1
            else:
                return False
        return True
