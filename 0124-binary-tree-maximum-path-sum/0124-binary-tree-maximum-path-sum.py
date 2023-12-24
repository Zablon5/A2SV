# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def maxsum(root,sm):
            if root:
                lsm=max(0,maxsum(root.left,sm))
                rsm=max(0,maxsum(root.right,sm))
                sm[0]=max(sm[0],lsm+rsm+root.val)
                return root.val+max(lsm,rsm)
            return 0
        sm=[-float('inf')]
        maxsum(root,sm)
      
        return sm[0]
        