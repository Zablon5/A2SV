# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        nextCurr = head.next

        while nextCurr:
            if nextCurr.val == curr.val:
                nextCurr = nextCurr.next 
                if not nextCurr:
                    prev.next = nextCurr 
            else:
                if curr.next != nextCurr:
                    prev.next = nextCurr
                    curr = nextCurr
                    nextCurr = nextCurr.next

                else:
                    prev=prev.next
                    curr = curr.next
                    nextCurr = nextCurr.next

        
        return dummy.next
        
        