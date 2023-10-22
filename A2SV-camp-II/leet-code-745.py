class TrieNode:
    def __init__(self):
        self.children={}
        self.index=[]
class WordFilter:

    def __init__(self, words: List[str]):
        self.root1=TrieNode()
        self.root2=TrieNode()
        for i,word in enumerate(words):
            self.insert(word,i)
            self.insert2(word[::-1],i)
    def insert(self,word,i):
        curr_node=self.root1
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c]=TrieNode()
            curr_node=curr_node.children[c]
            curr_node.index.append(i)
    def insert2(self,word,i):
        curr_node=self.root2
        for c in word:
            if c not in curr_node.children:
                curr_node.children[c]=TrieNode()
            curr_node=curr_node.children[c]
            curr_node.index.append(i)         
                 
    def f(self, pref: str, suff: str) -> int:
        curr_node=self.root1

        for c in pref:
            if c not in curr_node.children:
                return -1
            curr_node=curr_node.children[c]
        pre_ind=curr_node.index
        curr_node=self.root2
        for c in suff[::-1]:
            if c not in curr_node.children:
                return -1
            curr_node=curr_node.children[c]
        suff_ind=curr_node.index
        for i in pre_ind[::-1]:
            if i in suff_ind:
                return i
        return -1            

        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(pref,suff)
