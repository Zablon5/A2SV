class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups=defaultdict(list)
        for i,word in enumerate(strs):
            groups[''.join(sorted(list(word)))].append(strs[i])
            
        return [group for group in groups.values()]   
