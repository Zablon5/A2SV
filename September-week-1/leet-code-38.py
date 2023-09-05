"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hmap={None:None}     
        current=head
        while current:
            copy=Node(current.val)
            hmap[current]=copy
            current=current.next
        current=head
        while current:
            copy=hmap[current]
            copy.next=hmap[current.next]
            copy.random=hmap[current.random]
            current=current.next
        return hmap[head] 
