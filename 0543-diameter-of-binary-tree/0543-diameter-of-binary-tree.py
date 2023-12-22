# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def solve(root,ans):
            if root:
                lh=solve(root.left,ans)
                rh=solve(root.right,ans)
                ans[0]=max(ans[0],lh+rh)
                return 1+max(lh,rh)
            return 0
        ans=[0]
        solve(root,ans)
        return ans[0]
        