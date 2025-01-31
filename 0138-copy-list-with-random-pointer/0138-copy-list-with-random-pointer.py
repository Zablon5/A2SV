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
        temp = head
        while temp:
        
            tmp = temp.next
            newNode = Node(temp.val)
            temp.next = newNode
            newNode.next = tmp
            temp = temp.next.next
        temp = head

        while temp:
            copy = temp.next
            random = temp.random

            if random == None:
                copy.random = None
            else:
                copy.random = random.next
            
            temp = temp.next.next
        dummy = Node(-1)
        tmp = dummy
        temp = head
        while temp:
            tmp.next = temp.next
            tmp = tmp.next
            temp.next = temp.next.next
            temp = temp.next
        return dummy.next

        
        
        