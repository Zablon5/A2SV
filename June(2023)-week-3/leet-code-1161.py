# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q=deque([root])
        ans=[]
        while q:
            sm=0
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    sm+=node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)    
            ans.append(sm)     
        return ans.index(max(ans))  +1         
        
