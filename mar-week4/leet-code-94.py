# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def inorder(root,result):
            if root==None:
                return
            inorder(root.left,result) 
            result.append(root.val)  
            inorder(root.right,result) 
        result=[]
        inorder(root,result)   
        return result 
        
