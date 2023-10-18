class TrieNode:
    def __init__(self):
        self.value=0
        self.children={}
        self.flag=False
        self.wordVal=0
class MapSum:

    def __init__(self):
        self.root=TrieNode()
    def does_exit(self,word):
   
        curr_node=self.root
        for c in word:
            if c not in curr_node.children:
                return [False,0]
            curr_node=curr_node.children[c]
        ans = [curr_node.flag,curr_node.wordVal]  
        return ans      

    def insert(self, key: str, val: int) -> None:
        curr_node=self.root
        ans=self.does_exit(key)
        if ans[0]:
            
            for c in key:
                curr_node=curr_node.children[c]
                curr_node.value=curr_node.value-ans[1]+val
            curr_node.wordVal=val    
              
                
        else:
            for c in key:
                if c not in curr_node.children:
                    curr_node.children[c]=TrieNode()
                
                curr_node=curr_node.children[c] 
                curr_node.value+=val  
            curr_node.wordVal=val 
            curr_node.flag=True 
                
        

    def sum(self, prefix: str) -> int:
        
        curr_node=self.root
        for c in prefix:
            if c in curr_node.children:
                curr_node=curr_node.children[c]
            else:
                return 0 
               
        return curr_node.value    
    
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
