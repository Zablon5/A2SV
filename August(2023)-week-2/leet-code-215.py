class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nm=sorted(nums)
        return nm[-k]
