# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #Find mid point
        slow=head
        fast=head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        #Slice 
        second = slow.next
        slow.next=None

        #Reverse second half
        prev=None
        
        while second:
            next_node=second.next
            second.next=prev
            prev=second
            second=next_node
        second=prev

        #merge two LinkedLists
        first=head
        while second:
            temp1=first.next
            temp2=second.next

            first.next=second
            second.next=temp1

            first=temp1
            second=temp2
        
        
