class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_counter = Counter(p)
        s_counter = Counter(s[:len(p)])
        result = []
        
        for i in range(len(s) - len(p) + 1):
            if s_counter == p_counter:
                result.append(i)
            s_counter[s[i]] -= 1
            if s_counter[s[i]] == 0:
                del s_counter[s[i]]
            if i + len(p) < len(s):
                s_counter[s[i + len(p)]] += 1
                
        return result
