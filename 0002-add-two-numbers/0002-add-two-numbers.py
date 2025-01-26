# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-1)
        temp = dummy
        carry = 0
        while l1 or l2:
            sm = carry
            carry = 0
            if l1:
                sm+=l1.val
                l1=l1.next
            if l2:
                sm+=l2.val
                l2=l2.next
            if sm>=10:
                sm-=10
                carry = 1
            newNode = ListNode(sm)
            temp.next = newNode
            temp = newNode
        if carry:
            temp.next = ListNode(1)
        return dummy.next

