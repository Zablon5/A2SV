# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        

        def mergeK(n, lists):
            
            if n == len(lists) - 1:
                return lists[-1]
            merged = mergeK(n+1, lists)
            ans = merge(lists[n], merged)
            print("ans")
            return ans


        def merge(head1, head2):
            sortedHead = ListNode(-1)
            temp = sortedHead
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
            return sortedHead.next
        if len(lists) == 0:
            return None
        return mergeK(0, lists)
        
            
                    
                


        