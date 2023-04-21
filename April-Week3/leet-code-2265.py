# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res=0
        def rec(root):
            if not root:
                return 0,0
            lsum,lcount=rec(root.left)
            rsum,rcount=rec(root.right) 
            totsum=root.val + lsum +rsum
            totcount=1+lcount+rcount
            if totsum // totcount == root.val:
                self.res+=1
            return totsum,totcount
        rec(root)
        return self.res 
