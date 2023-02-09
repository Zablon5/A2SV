class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        n = len(fruits)
        i = 0
        j = 0
        count = {}
        max_count = 0
        while j < n:
            if fruits[j] in count:
                count[fruits[j]] += 1
            else:
                count[fruits[j]] = 1
            while len(count) > 2:
                count[fruits[i]] -= 1
                if count[fruits[i]] == 0:
                    del count[fruits[i]]
                i += 1
            max_count = max(max_count, j - i + 1)
            j += 1
        return max_count
