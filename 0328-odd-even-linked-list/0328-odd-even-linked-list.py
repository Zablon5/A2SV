# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        odd = head 
        even = head.next
        tempEven = head.next

        while odd:
            if odd.next:
                tmp = odd.next.next
                odd.next = odd.next.next
                if tmp:
                    odd = tmp
            else:
                break
            if even and even.next:
                tmp2 = even.next.next
                even.next = even.next.next
                even = tmp2
        odd.next = tempEven

        return head

            

        
            
        