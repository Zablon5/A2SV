# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root,ma,mi):
            if not root:
                return True
            if mi<=root.val or root.val<=ma:
                return False
            return validate(root.left,ma,min(mi,root.val)) and validate(root.right,max(ma,root.val),mi)   
        return validate(root,-inf,inf)    
        
