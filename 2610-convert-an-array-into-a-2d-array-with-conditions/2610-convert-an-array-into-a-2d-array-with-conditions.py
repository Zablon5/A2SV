class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = Counter(nums)
        n = max(freq.values())
        ans=[]
        
        for _ in range(n):
            minians=[]
            for i in freq:
                if freq[i]:
                    minians.append(i)
                    freq[i]-=1
            ans.append(minians)
        return ans
                
            
        