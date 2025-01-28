# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        n = 0
        if not head or not head.next or k==0:
            return head
        temp = head

        while temp:
            n += 1
            temp = temp.next
        swapPos = n - k%n
        if k==n or swapPos == n:
            return head
        

        pos = head
        prev = None
        for _ in range(swapPos):
            prev = pos
            pos = pos.next
            
        temp = head
        while temp:
            if temp == prev:
                temp.next = None
            temp = temp.next
        dummy = ListNode(-1, pos)
        while pos and pos.next:
            pos = pos.next
        pos.next = head
        return dummy.next
            

        