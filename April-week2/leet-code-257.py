# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans_path=[]
        path=[]
        def paths(root,path):
            path.append(root.val)
            if not(root.left or root.right):
                f_path=[]
                for i in path:
                    f_path.append(str(i))
                ans="->".join(f_path) 
                ans_path.append(ans)    
            if root.left:
                paths(root.left,path)
            if root.right:
                paths(root.right,path)
            path.pop()
        
        paths(root,path)
        return ans_path
