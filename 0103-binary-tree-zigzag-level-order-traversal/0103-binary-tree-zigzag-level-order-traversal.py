# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        def bfs(root,ans):
            q=deque()
            if root:
                q.append(root)
            flag=0
            while q:
                n=len(q)
                mini=[]
                for _ in range(n):
                    node=q.popleft()
                    mini.append(node.val)
                    if node.right:
                        q.append(node.right)
                    if node.left:
                        q.append(node.left)
                if flag==1:
                    ans.append(mini)
                    flag=0
                else:
                    ans.append(mini[::-1])
                    flag=1
        ans=[]
        bfs(root,ans)
        return ans
        