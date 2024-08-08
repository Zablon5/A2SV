# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        mp=defaultdict(list)
        
        def traverse(root,row,col):
            if root:
                mp[col].append((row,root.val))
                if root.left:
                    traverse(root.left,row+1,col-1)
                if root.right:
                    traverse(root.right,row+1,col+1)
                
                
        traverse(root,0,0)
        ans=[]
        for i in sorted(mp.keys()):
            lst=mp[i]
            lst.sort()
            ans.append([val for row,val in lst])

        return ans

        