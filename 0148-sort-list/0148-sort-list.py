# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        size = 0
        temp = head

        while temp:
            size+=1
            temp = temp.next
   
        def merge(head1, head2):
            merged = ListNode(-1)
            temp = merged
            while head1 and head2:
                if head1.val <= head2.val:
                    temp.next = head1
                    temp = head1
                    head1 = head1.next
                else:
                    temp.next = head2
                    temp = head2
                    head2 = head2.next
            if head1:
                temp.next = head1
            else:
                temp.next = head2
            return merged.next
        def midPoint(leftH, n):
            count = 0
            temp = leftH
            rightH = None
            while temp:
                count += 1
                if count == n:
                    rightH = temp.next
                    temp.next = None
                temp = temp.next
            return [leftH, rightH]
        k = size
        def mergeSort(head, size):
            if not head or not head.next:
                return head
            left, right = midPoint(head, size//2)
            sortedL = mergeSort(left, size//2)
            sortedR = mergeSort(right, k - size//2)

            return merge(sortedL, sortedR)
        return mergeSort(head,size)




        