class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph=defaultdict(list)
        for i,(u,v) in enumerate(edges):
            graph[v].append([u,succProb[i]])
            graph[u].append([v,succProb[i]])
        if end_node not in graph:
            return 0    
        probs={node:0 for node in graph}   
        probs[start_node]=-1
        heap=[(-1,start_node)]
        while heap:
            curr_prob,curr_node=heappop(heap)
            for next_node,next_prob in graph[curr_node]:
                new_prob=next_prob*curr_prob
                if new_prob<probs[next_node]:
                    probs[next_node]=new_prob
                    heappush(heap,(new_prob,next_node))
        print(probs)            
        return -probs[end_node] 
