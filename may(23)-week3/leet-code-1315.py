# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.ans=0
        def dfs(root,parent,gparent):
            if not root: 
                return
            if parent and gparent and gparent.val%2==0:
                self.ans+=root.val
            dfs(root.left,root,parent)     
            dfs(root.right,root,parent)   
        dfs(root,None,None)    
        return self.ans 
