class TrieNode:
    def __init__(self):
        self.children={}
        self.flag=False
class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        cur_node=self.root
        for c in word:
            if c not in cur_node.children:
                cur_node.children[c]=TrieNode()
            cur_node=cur_node.children[c]
        cur_node.flag=True        

    def search(self, word: str) -> bool:
        def dfs(i,root):
            cur_node=root
            for j in range(i,len(word)):
                w=word[j]
                if w=='.':
                    for child in cur_node.children.values():
                        if dfs(j+1,child):
                            return True
                    return False    
                else:
                    if w not in cur_node.children:
                        return False
                    cur_node=cur_node.children[w]  
            return cur_node.flag   
        return dfs(0,self.root)         
