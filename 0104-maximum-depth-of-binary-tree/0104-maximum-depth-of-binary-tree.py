# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        ans=0
        if not root:
            return 0
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                
                if node.left:q.append(node.left)
                if node.right:q.append(node.right)
            ans+=1
        return ans
            
        