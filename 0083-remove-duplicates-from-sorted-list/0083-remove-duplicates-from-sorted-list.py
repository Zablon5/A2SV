# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        cur = head
        nextCur = head.next

        while nextCur:
            if cur.val == nextCur.val:
                nextCur = nextCur.next
                if not nextCur:
                    cur.next = nextCur

            else:
                cur.next = nextCur
                nextCur = nextCur.next
                cur = cur.next
        return head


        