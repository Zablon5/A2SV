class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n=len(nums)
        if n<2:
            return 0
        def radix_sort(arr):
            max_digits = len(str(max(arr)))
            for digit in range(max_digits):
                arr = counting_sort_by_digit(arr, digit)
            return arr

        def counting_sort_by_digit(arr, digit):
            counting_array = [0] * 10
            output = [0] * len(arr)

            for num in arr:
                digit_value = (num // 10**digit) % 10
                counting_array[digit_value] += 1

            for i in range(1, 10):
                counting_array[i] += counting_array[i - 1]

            for num in reversed(arr):
                digit_value = (num // 10**digit) % 10
                output[counting_array[digit_value] - 1] = num
                counting_array[digit_value] -= 1

            return output    
        sorted_nums=radix_sort(nums) 
        l=0
        r=1
        mx=0
        while r<n:
            mx=max(mx,sorted_nums[r]-sorted_nums[l])
            r+=1
            l+=1
        return mx 
