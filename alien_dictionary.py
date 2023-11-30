from collections import defaultdict
class Solution:
    def findOrder(self,alien_dict, N, K):
        adj=defaultdict(list)
        for j in range(N-1):
            word1=alien_dict[j]
            word2=alien_dict[j+1]
            n1=len(word1)
            n2=len(word2)
            for i in range(min(n1,n2)):
                if word1[i]!=word2[i]:
                    adj[ord(word1[i])-97].append(ord(word2[i])-97)
                    break
      
        ans=[]
        visited=[0 for _ in range(K)]
        path=[0 for _ in range(K)]
        def dfs(node):
            
            for child in adj[node]:
                if not visited[child]:
                  
                    visited[child]=1
                    dfs(child)
                        
            ans.append(chr(node+97))  
          
        for i in range(K):
            if not visited[i]:
                
                visited[i]=1
                dfs(i)
               
        return ans[::-1]
