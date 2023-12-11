# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hmap={}
        ans=[False]
        def traverse(root,need):
            if root:
                target=k-root.val
                if target
        
                hmap[root.val]=k-root.val
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)
        
        traverse(root)
        return ans[0]
