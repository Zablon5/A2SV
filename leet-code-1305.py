# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        ans=[]
        def traverse(root):
           
            if root:
                ans.append(root.val)
                if root.left:
                    traverse(root.left)
                if root.right:
                    traverse(root.right)   
            return     
        traverse(root1)
        traverse(root2)
        ans.sort()
        return ans
