# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
      
        prev = slow
        cur = slow.next
        
        
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
      
        slow.next = None
        temp = head
       
        while temp:
            
            tmpnxt = temp.next
            prevnxt = prev.next

            temp.next = prev
            
            if not prevnxt:
                temp = prev
                temp.next = None
                break
            prev.next = tmpnxt
            temp = tmpnxt
            prev = prevnxt
