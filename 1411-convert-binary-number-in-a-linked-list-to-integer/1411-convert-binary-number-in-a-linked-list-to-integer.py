# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        ans = 0
        while head:
            ans += (head.val)*(2**(n-1))
            n -= 1
            head = head.next
        return ans
        