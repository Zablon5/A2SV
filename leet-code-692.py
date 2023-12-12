class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        count=Counter(words)
        pair=[(-count[i],i) for i in count]
       
        heapq.heapify(pair)
        ans=[]
        for i in range(k):
            freq,val=heappop(pair)
            ans.append(val)
        return ans
