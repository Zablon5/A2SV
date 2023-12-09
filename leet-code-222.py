# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        mx=[0]
        def traverse(root):
            if root:
                mx[0]+=1
                if root.right:
                    traverse(root.right)
                if root.left:
                    traverse(root.left)
            
        traverse(root)
        return mx[0]
        
        
