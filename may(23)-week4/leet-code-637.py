# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q=deque()
        q.append(root)
        if not (root.left or root.right):
            return [root.val]
        ans=[]
        while q:
            sm=0
            n=0
            
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    
                    sm+=node.val
                    n+=1
                    if node.left:
                        q.append(node.left)
                    if node.right:    
                        q.append(node.right)
            
            ans.append(sm/n)        
        return ans    
