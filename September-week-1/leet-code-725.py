# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count=0
        current=head
        ans=[]
        
        while current:
            count+=1
            current=current.next
        part=count//k
        remainder=count%k    
        current=head
        if k>=count:
            while current:
                temp=current.next
                current.next=None
                ans.append(head)
                head=temp
                current=head
            for i in range(k-count):
                ans.append(None)    
            return ans 
                   
                
        for i in range(k):
            dum=part
            current=head
            if remainder:
                
                while current and dum:
                    current=current.next
                    dum-=1
                temp=current.next
                current.next=None
                ans.append(head)
                head=temp
                remainder-=1
                
            else:
                
                current=head
                dum-=1
                while current and dum:
                    current=current.next
                    dum-=1
                print(part)    
                temp=current.next
                current.next=None
                ans.append(head)
                head=temp

        return ans
