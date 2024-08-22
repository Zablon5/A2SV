class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        ans = []
        for num in nums:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)
        n = len(pos)
        for i in range(n):
            ans.append(pos[i])
            ans.append(neg[i])
        return ans