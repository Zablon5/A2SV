# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ans=[]
        def traverse(root):
            if root:
                traverse(root.left)
                ans.append(root.val)
                traverse(root.right)
        traverse(root)
        suff=[0]*(len(ans)+1)
        for i in range(len(ans)-1,-1,-1):
            suff[i]=ans[i]+suff[i+1]
        def traverse(root):
            if root:
                traverse(root.left)
                root.val=suff.pop(0)
                traverse(root.right)
        traverse(root)
        return root
