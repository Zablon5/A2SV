class Solution:
    def rob(self, nums: List[int]) -> int:
        def smartRobber(i, nums, memo):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            oneStepRob = nums[i] + smartRobber(i+2, nums, memo)
            twoStepRob = nums[i] + smartRobber(i+3, nums, memo)
            memo[i] = max(oneStepRob, twoStepRob)
            return memo[i]
        if len(nums) <= 2:
            return max(nums)
        memo = {}
        ans = 0
        for i in range(len(nums)):
            ans = max(smartRobber(i, nums, memo), ans)

        return ans
        