# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        def calculateLength(head):
            length = 0
            temp = head
            while temp:
                length += 1
                temp = temp.next
            return length
        lenA = calculateLength(headA)
        lenB = calculateLength(headB)

        def alignHead(head, n):
            for _ in range(n):
                head = head.next
            return head
        if lenA > lenB:
            headA = alignHead(headA, lenA-lenB)
        else:
            headB = alignHead(headB, lenB-lenA)

        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

        
            


    
        