# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode, start: int) -> int:
        q=deque()
        chiledparent={}
        q.append(root)
        startnode=None
        visited=set()
        
        if root.val==start:
            startnode=root
        while q:
            node=q.popleft()
            if node.left:
                if node.left.val==start:
                    startnode=node.left
                chiledparent[node.left]=node
                q.append(node.left)
            if node.right:
                if node.right.val==start:
                    startnode=node.right
                chiledparent[node.right]=node
                q.append(node.right)
        visited.add(startnode)
        q.append(startnode)
     
        ans=0
        while q:
            n=len(q)
            for i in range(n):
                node=q.popleft()
                if node in chiledparent and chiledparent[node] not in visited:
                    visited.add(chiledparent[node])
                    
                    q.append(chiledparent[node])
                if node.left and node.left not in visited:
                    visited.add(node.left)
                    q.append(node.left)
                if node.right and node.right not in visited:
                    visited.add(node.right)
                    q.append(node.right)
            ans+=1
                
        return ans-1
                
        
        