class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occurence=Counter(arr).values()
       
        return len(occurence)==len(set(occurence))
        