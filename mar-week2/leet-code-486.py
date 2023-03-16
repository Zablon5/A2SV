class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def helper(nums, i, j):
            if i == j:
                return nums[i]
            else:
                return max(nums[i] - helper(nums, i+1, j), nums[j] - helper(nums, i, j-1))

        return helper(nums, 0, len(nums)-1) >= 0
