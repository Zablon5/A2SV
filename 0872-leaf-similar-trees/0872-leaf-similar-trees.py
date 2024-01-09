# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def inorder(root,ans):
            if root:
                inorder(root.left,ans)
                if not root.right and not root.left:
                    ans.append(root.val)
                inorder(root.right,ans)
        ans1=[]
        ans2=[]
        inorder(root1,ans1)
        inorder(root2,ans2)
        n1,n2 = len(ans1),len(ans2)
        if n1!=n2:
            return False
        for i in range(n1):
            if ans1[i]!=ans2[i]:
                return False
        return True
            
        