class Solution:
    def minimumPushes(self, word: str) -> int:
        count = Counter(word)
        count_ls = []
        for i in count:
            count_ls.append([count[i],i])
        count_ls.sort()
        
        round, assigned, ans = 1, 1, 0
        for cnt,char in count_ls[::-1]:
            
            if assigned <= 8:
                round = 1
            elif assigned <= 16:
                round = 2
            elif assigned <= 24:
                round = 3
            else:
                round = 4
          
            assigned += 1
            ans += count[char]*round
                
        return ans