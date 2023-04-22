# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.ans=0
        lookup=collections.defaultdict(int)
        lookup[0]=1
        def help(root,cursum):
            if not root:
                return
            cursum+=root.val
            self.ans+=lookup[cursum-targetSum]    
            lookup[cursum]+=1
            help(root.left,cursum)
            help(root.right,cursum)
            lookup[cursum]-=1
        help(root,0)
        return self.ans    
