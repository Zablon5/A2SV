# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def converter(root):
            if not root:
                return []
            return converter(root.left) +[root.val] + converter(root.right)
        ext=converter(root)    
        return ext[k-1]
