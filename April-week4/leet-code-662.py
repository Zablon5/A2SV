# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        inilev,ininum,maxwidth=1,1,0
        queue=deque([[inilev,ininum,root]])
        while queue:
            [num,level,node]=queue.popleft()
            if level>inilev:
                inilev,ininum=level,num
            maxwidth=max(maxwidth,num-ininum+1)
            if node.left:
                queue.append([num*2,level+1,node.left])
            if node.right:
                queue.append([num*2+1,level+1,node.right])
        return maxwidth  
