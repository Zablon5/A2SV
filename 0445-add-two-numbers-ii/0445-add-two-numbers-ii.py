# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            cur = head

            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev
        head1 = reverse(l1)
        head2 = reverse(l2)

        dummy = ListNode(-1)
        temp = dummy
        carry = 0

        while head1 and head2:
            sm = head1.val + head2.val + carry
            if sm>9:
                carry = 1
                val = sm - 10
            else:
                carry = 0
                val = sm
            newNode = ListNode(val)
            temp.next = newNode
            temp = newNode
            head1 = head1.next
            head2 = head2.next
        if carry == 0:
            if head1:
                temp.next = head1
            else:
                temp.next = head2
        else:
            while head1:
                sm = head1.val + carry
                if sm>9:
                    carry = 1
                    val = sm - 10
                else:
                    carry = 0
                    val = sm
                newNode = ListNode(val)
                temp.next = newNode
                temp = newNode
                head1 = head1.next
            while head2:
                sm = head2.val + carry
                if sm>9:
                    carry = 1
                    val = sm - 10
                else:
                    carry = 0
                    val = sm
                newNode = ListNode(val)
                temp.next = newNode
                temp = newNode
                head2 = head2.next
            if carry:
                temp.next = ListNode(1)

        return reverse(dummy.next)

        