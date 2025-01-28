# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        tempA = headA
        tempB = headB

        while tempA or tempB:
            if tempA == tempB:
                return tempA
            if (not tempA.next) and tempB.next:
                tempA = headB
                tempB = tempB.next
            elif (not tempB.next) and tempA.next:
                tempB = headA
                tempA = tempA.next
            else:
                tempA = tempA.next
                tempB = tempB.next
        return None

            
        
        

        
            


    
        