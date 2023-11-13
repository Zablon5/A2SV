# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hset=set()
        current=head
        while current:
            if current.val=='visited':
                return True
            else:
                current.val='visited'
                current=current.next
               
        return False
