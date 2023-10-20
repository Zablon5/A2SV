class TrieNode:
    def __init__(self):
        self.children={}
        self.val=0

class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,words):
        
        for word in words:
            curr_node=self.root
            for c in word:
                if c not in curr_node.children:
                    curr_node.children[c]=TrieNode()
                curr_node=curr_node.children[c]
                curr_node.val+=1



    def sumPrefixScores(self, words: List[str]) -> List[int]:
        self.insert(words)
        ans=[]
        for word in words:
            curr_node=self.root
            ans_sum=0
            for c in word:
                curr_node=curr_node.children[c]
                ans_sum+=curr_node.val
            ans.append(ans_sum)   
        return ans     
