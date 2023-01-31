class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, 0
        A = len(nums)
        numbzer = 0
        max_len = 0
        while r < A:
            if nums[r] == 0:
                numbzer += 1
            while numbzer > k:
                if nums[l] == 0:
                    numbzer -= 1
                l += 1
            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len          
