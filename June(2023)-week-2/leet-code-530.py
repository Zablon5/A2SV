# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        li=[]
        def traverse(root,li):
            
            if root:
                traverse(root.left,li)
                li.append(root.val)
                traverse(root.right,li)
        traverse(root,li)        
        ans=10**5+1
        for i in range(1,len(li)):
            ans=min(ans,abs(li[i-1]-li[i]))  
        return ans    
