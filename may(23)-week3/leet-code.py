# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        def converter(root):
            if not root:
                return []
            return converter(root.left) +[root.val] + converter(root.right)
        new=converter(root)
        def DAC(l,r):
            if l>r:
                return None
            mid=(l+r)//2    
            return TreeNode(new[mid],DAC(l,mid-1),DAC(mid+1,r)) 
        return DAC(0,len(new)-1)   
