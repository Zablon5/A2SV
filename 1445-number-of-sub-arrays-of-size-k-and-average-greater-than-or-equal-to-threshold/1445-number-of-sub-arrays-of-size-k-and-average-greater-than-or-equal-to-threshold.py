class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l, r = 0, k - 1
        n = len(arr)
        ans = 0
        sm = sum(arr[l:k])
        while r < n:
            if sm / k >= threshold:
                ans += 1
            sm -= arr[l]
            l += 1
            r += 1
            if r < n:
                sm += arr[r]
        return ans

        