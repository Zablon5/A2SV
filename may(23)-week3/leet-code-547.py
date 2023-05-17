class Solution:
    
    def findCircleNum(self, isConnected):
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)

        numofprov=0
        visited=set()
        for start in range(len(isConnected)):
            if start not in visited:
                numofprov+=1
                dfs(start)
        return numofprov
