# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        q=deque()
        q.append(root)
        ans=[]
        rans=[]
        while q:
            level=[]
            for i in range(len(q)):
                node=q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:        
                ans.append(level)   
        for i in range(len(ans)):
            if i%2==0:
                rans.append(ans[i])
            else:
                rans.append(ans[i][::-1])    

        return rans    
                
