# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        lessThanX = ListNode(-1)
        greaterThanX = ListNode(-1)
        lessTemp = lessThanX
        greaterTemp = greaterThanX
        temp = head

        while temp:
            if temp.val < x:
                lessTemp.next = temp
                lessTemp = temp
                
                
            else:
                greaterTemp.next = temp
                greaterTemp = temp
                

            temp = temp.next
        
        
        if greaterTemp.next:
            greaterTemp.next = None
        if lessTemp.next:
            lessTemp.next = None
        lessTemp.next = greaterThanX.next
        return lessThanX.next
            

        