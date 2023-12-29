class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or k == 1:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        
        prev = dummy
        curr = head
        count = 0
        
        while curr:
            count += 1
            if count % k == 0:
                prev = self.reverse(prev, curr.next)
                curr = prev.next
            else:
                curr = curr.next
        return dummy.next

    def reverse(self, prev: Optional[ListNode], next: Optional[ListNode]) -> Optional[ListNode]:
        last = prev.next
        curr = last.next
        while curr != next:
            last.next = curr.next
            curr.next = prev.next
            prev.next = curr
            curr = last.next
        return last