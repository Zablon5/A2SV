class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            y,x=heapq.heappop(heap),heapq.heappop(heap)
            if x==y:
                continue
            else:
                heapq.heappush(heap,y-x)  
            print(heap)     
        if len(heap)==0:
            return 0      
        return -heap[0]        
