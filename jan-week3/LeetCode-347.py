class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        result=[]
        for i,j in count.most_common(k):
            result.append(i)
        return result    
