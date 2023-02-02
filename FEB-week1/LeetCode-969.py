class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sub_array, k):
            sub_array[:k] = sub_array[:k][::-1]

        res = []
        n = len(arr)
        for i in range(n, 0, -1):
            max_idx = arr.index(max(arr[:i]))
            if max_idx != i-1:
                if max_idx != 0:
                    flip(arr, max_idx+1)
                    res.append(max_idx+1)
                flip(arr, i)
                res.append(i)
        return res

        
