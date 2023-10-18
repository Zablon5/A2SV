class TrieNode:
    def __init__(self):
        self.children={}
        self.flag=False
class Solution:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        curr_node=self.root
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c]=TrieNode()    
            curr_node=curr_node.children[c]   
        curr_node.flag=True   
    def does_pref_exist(self,word):
        fl=True
        curr_node=self.root  
        for c in word:
            if c not in curr_node.children:
                return False
            else:
                curr_node=curr_node.children[c]
                fl=fl and curr_node.flag
        return fl        
    def longestWord(self, words: List[str]) -> str:
        longest=''
        for word in words:
            self.insert(word)
        for word in words:
            if self.does_pref_exist(word):
                if len(word)>len(longest):
                    longest=word
                if len(word)==len(longest) and word<longest:
                    longest=word
        return longest            
